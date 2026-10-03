#!/usr/bin/env python3
"""
KNTQ Season 2 claim tracker  (READ-ONLY: only eth_blockNumber / eth_getLogs / eth_call
and the public Hyperliquid info API; never signs or sends anything).

What it measures (incrementally, so it is cheap to run every 2 hours):
  * unique claimer wallets, number of claim txs, total KNTQ claimed, total USDC paid
    -> summed from Claimed(address indexed sender, uint256 amount, uint256 cost) events of the
       Kinetiq "CKNTQ" Season-2 claim contract (verified source on hyperevmscan; the contract keeps
       no running total, only a per-wallet `claimed(address)` mapping)
  * KNTQ funded into the contract (sum of KNTQ Transfer events INTO the contract)
  * KNTQ still in the contract and USDC collected (balanceOf via eth_call)
  * % of the funded S2 pool claimed; % of eligible wallets that claimed (if ELIGIBLE_WALLETS known)
  * KNTQ spot price: HyperCore KNTQ/USDC orderbook mid ("@334") via the info API, plus the
    HyperEVM KNTQ/USDC pool price (slot0) that the claim contract itself references

Usage:
  python3 kntq_s2_tracker.py                      # incremental run, prints JSON + appends CSV
  python3 kntq_s2_tracker.py --rpc URL            # use a different HyperEVM RPC
  python3 kntq_s2_tracker.py --reset              # forget state and backfill from deployment
State/CSV default to files next to this script (override with --state / --csv).
Only depends on the Python standard library (works through HTTPS_PROXY env var).
"""
import argparse, csv, datetime, json, os, sys, time, urllib.request, urllib.error

# ---------------------------------------------------------------- constants (verified on-chain)
CHAIN_ID       = 999
CLAIM          = "0x435bb7ea4eb481cb686606d089ea4dee4c6cc03b"  # CKNTQ proxy (TransparentUpgradeableProxy)
CLAIM_IMPL     = "0xedfd49704f6f0abafac376f35270c4c7585d40e9"  # CKNTQ implementation (verified)
KNTQ           = "0x000000000000780555bd0bca3791f89f9542c2d6"  # KNTQ ERC-20, 18 decimals
USDC           = "0xb88339cb7199b77e23db6e890353e22632ba630f"  # native USDC on HyperEVM, 6 decimals
POOL           = "0x99cb209d412cbf9f525b6002d2c975b52bd2bd08"  # KNTQ/USDC v3-style pool (token0=KNTQ, token1=USDC)
DEPLOY_BLOCK   = 47315563                                       # proxy creation block (2026-09-30 19:27 UTC)
CLAIM_START    = 1790856000                                     # 2026-10-01 12:00:00 UTC (start())
CLAIM_END      = 1791720000                                     # 2026-10-11 12:00:00 UTC (end())
CLAIM_PRICE    = 0.261331                                       # quote(1e18)/1e6 USDC per KNTQ
SPOT_PAIR      = "@334"                                         # HyperCore KNTQ/USDC spot pair (spot() == 334)
ELIGIBLE_WALLETS = None    # denominator: set to the official eligible-wallet count once published
TOTAL_ALLOCATION = 50_000_000  # official S2 size (KNTQ); cross-checked against funding transfers

T_CLAIMED   = "0x987d620f307ff6b94d58743cb7a7509f24071586a77759b77c2d4e29f75a2f9a"  # Claimed(address,uint256,uint256)
T_WITHDRAWN = "0xd1c19fbcd4551a5edfb66d43d2e337c04837afda3482b42bdf569a8fccdae5fb"  # Withdrawn(address,address,uint256)
T_BRIDGED   = "0x74fb16e5070973b8b25c03b8e789b5102782e16d3d3843b8b6cbaafbca1108a7"  # Bridged(address,uint64)
T_TRANSFER  = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"  # ERC-20 Transfer

# Tested 2026-10-03 from a cloud sandbox (see notes). All public, no API key.
DEFAULT_RPCS = [
    "https://hyperliquid-rpc.publicnode.com",  # 1000-block getLogs cap, ~0.25 s, served 2-day-old ranges fine
    "https://rpc.hypurrscan.io",               # 1000-block cap, ~0.9 s
    "https://rpc.hyperliquid.xyz/evm",         # official; 1000-block cap; timed out (5 s) on 2-day-old ranges
    "https://rpc.purroofgroup.com",            # accepted 10,000-block ranges (community-run)
]
INFO_API  = "https://api.hyperliquid.xyz/info"
MAX_RANGE = 1000
PACE_S    = float(os.environ.get("KNTQ_PACE", "0.65"))  # seconds between RPC calls (~90 req/min)

HERE = os.path.dirname(os.path.abspath(__file__))


def post(url, payload, retries=6):
    data = json.dumps(payload).encode()
    delay = 2.0
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, headers={"content-type": "application/json",
                                                               "user-agent": "kntq-s2-tracker/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(delay); delay *= 2; continue
            raise
        except (urllib.error.URLError, TimeoutError):
            if attempt < retries - 1:
                time.sleep(delay); delay *= 2; continue
            raise


class Rpc:
    """JSON-RPC client with ordered fail-over across several public endpoints."""
    def __init__(self, urls):
        self.urls = list(urls)
        self.calls = 0

    def __call__(self, method, params, urls=None):
        last = None
        for url in (urls or self.urls):
            time.sleep(PACE_S)
            self.calls += 1
            try:
                r = post(url, {"jsonrpc": "2.0", "id": self.calls, "method": method, "params": params})
            except Exception as e:          # network / HTTP error -> next endpoint
                last = f"{url}: {e}"
                continue
            if "error" in r:
                last = f"{url}: {r['error']}"
                continue
            return r["result"]
        raise RuntimeError(f"{method} failed on all RPCs; last error: {last}")


def pad(addr):
    return "0x" + addr[2:].lower().rjust(64, "0")


def balance_of(rpc, token, holder):
    return int(rpc("eth_call", [{"to": token, "data": "0x70a08231" + holder[2:].rjust(64, "0")}, "latest"]), 16)


def pool_price(rpc):
    """slot0().sqrtPriceX96 -> USDC per KNTQ (token0=KNTQ 18dp, token1=USDC 6dp)."""
    r = rpc("eth_call", [{"to": POOL, "data": "0x3850c7bd"}, "latest"])
    sq = int(r[2:66], 16)
    return (sq * sq / 2**192) * 1e12


def hl_price():
    mids = post(INFO_API, {"type": "allMids"})
    return float(mids[SPOT_PAIR]) if SPOT_PAIR in mids else None


def get_logs_window(rpc, flt, frm, to):
    """eth_getLogs for one window; on failure split the window in two (down to 50 blocks)."""
    try:
        return rpc("eth_getLogs", [dict(flt, fromBlock=hex(frm), toBlock=hex(to))])
    except RuntimeError:
        if to - frm + 1 <= 50:
            raise
        mid = (frm + to) // 2
        return get_logs_window(rpc, flt, frm, mid) + get_logs_window(rpc, flt, mid + 1, to)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rpc", action="append", help="HyperEVM RPC URL (repeatable; default: built-in fail-over list)")
    ap.add_argument("--state", default=os.path.join(HERE, "state.json"))
    ap.add_argument("--csv", default=os.path.join(HERE, "snapshots.csv"))
    ap.add_argument("--reset", action="store_true")
    ap.add_argument("--eligible", type=int, default=ELIGIBLE_WALLETS,
                    help="official eligible wallet count (denominator), if known")
    a = ap.parse_args()

    st = {"last_block": DEPLOY_BLOCK - 1, "wallets": {}, "claims": 0, "funded_wei": 0,
          "funding_txs": [], "withdrawn": [], "bridged": 0}
    if os.path.exists(a.state) and not a.reset:
        st = json.load(open(a.state))

    rpc = Rpc(a.rpc or ([os.environ["HYPEREVM_RPC"]] if os.environ.get("HYPEREVM_RPC") else DEFAULT_RPCS))
    latest = int(rpc("eth_blockNumber", []), 16)
    frm, to = st["last_block"] + 1, latest

    def on_claim_contract_log(lg):
        t0 = lg["topics"][0]
        if t0 == T_CLAIMED:
            who = "0x" + lg["topics"][1][-40:]
            amt = int(lg["data"][2:66], 16)
            cost = int(lg["data"][66:130], 16)
            w = st["wallets"].setdefault(who, [0, 0, 0])
            w[0] += amt; w[1] += cost; w[2] += 1
            st["claims"] += 1
        elif t0 == T_WITHDRAWN:
            st["withdrawn"].append({"token": "0x" + lg["topics"][1][-40:], "to": "0x" + lg["topics"][2][-40:],
                                    "amount": int(lg["data"][2:66], 16), "tx": lg["transactionHash"]})
        elif t0 == T_BRIDGED:
            st["bridged"] += int(lg["data"][2:66], 16)

    def on_kntq_in(lg):
        st["funded_wei"] += int(lg["data"][2:66], 16)
        st["funding_txs"].append({"from": "0x" + lg["topics"][1][-40:], "amount": int(lg["data"][2:66], 16),
                                  "block": int(lg["blockNumber"], 16), "tx": lg["transactionHash"]})

    n = 0
    cur = frm
    while cur <= to:                       # both filters per window, checkpoint after each window
        end = min(cur + MAX_RANGE - 1, to)
        for lg in get_logs_window(rpc, {"address": CLAIM, "topics": [[T_CLAIMED, T_WITHDRAWN, T_BRIDGED]]}, cur, end):
            on_claim_contract_log(lg)
        for lg in get_logs_window(rpc, {"address": KNTQ, "topics": [T_TRANSFER, None, pad(CLAIM)]}, cur, end):
            on_kntq_in(lg)
        st["last_block"] = end
        cur = end + 1
        n += 1
        if n % 20 == 0 or cur > to:
            json.dump(st, open(a.state, "w"))
            print(f"... scanned to block {end} ({len(st['wallets'])} wallets, {st['claims']} claims)", file=sys.stderr)

    kntq_left = balance_of(rpc, KNTQ, CLAIM) / 1e18
    usdc_held = balance_of(rpc, USDC, CLAIM) / 1e6
    try:
        evm_px = pool_price(rpc)
    except Exception:
        evm_px = None
    try:
        core_px = hl_price()
    except Exception:
        core_px = None

    wallets = st["wallets"]
    claimed = sum(v[0] for v in wallets.values()) / 1e18
    paid = sum(v[1] for v in wallets.values()) / 1e6
    funded = st["funded_wei"] / 1e18 or TOTAL_ALLOCATION
    now = datetime.datetime.now(datetime.timezone.utc)
    snap = {
        "utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "block": to,
        "unique_claimers": len(wallets),
        "claim_txs": st["claims"],
        "kntq_claimed": round(claimed, 2),
        "usdc_paid": round(paid, 2),
        "kntq_funded": round(funded, 2),
        "pct_of_pool_claimed": round(100 * claimed / funded, 3) if funded else None,
        "kntq_left_in_contract": round(kntq_left, 2),
        "usdc_held_by_contract": round(usdc_held, 2),
        "check_funded_minus_claimed_minus_left": round(funded - claimed - kntq_left, 4),
        "eligible_wallets": a.eligible,
        "pct_wallets_claimed": round(100 * len(wallets) / a.eligible, 3) if a.eligible else None,
        "kntq_px_core_mid": core_px,
        "kntq_px_evm_pool": round(evm_px, 6) if evm_px else None,
        "claim_price": CLAIM_PRICE,
        "premium_vs_claim_pct": round(100 * (core_px / CLAIM_PRICE - 1), 2) if core_px else None,
        "hours_left": round(max(0, CLAIM_END - now.timestamp()) / 3600, 2),
        "rpc_calls_this_run": rpc.calls,
    }

    # deltas vs the previous snapshot row, so a 2-hourly run is directly readable
    prev = None
    if os.path.exists(a.csv):
        rows = list(csv.DictReader(open(a.csv)))
        if rows:
            prev = rows[-1]
    if prev:
        dt_h = (now - datetime.datetime.strptime(prev["utc"], "%Y-%m-%dT%H:%M:%SZ")
                .replace(tzinfo=datetime.timezone.utc)).total_seconds() / 3600
        d_w = len(wallets) - int(prev["unique_claimers"])
        d_k = claimed - float(prev["kntq_claimed"])
        snap["since_prev_hours"] = round(dt_h, 2)
        snap["new_wallets"] = d_w
        snap["new_kntq_claimed"] = round(d_k, 2)
        snap["claim_pace_kntq_per_h"] = round(d_k / dt_h, 1) if dt_h > 0 else None
        # linear projection of the final claim share if this pace holds to the deadline
        snap["projected_pct_at_deadline"] = (
            round(100 * min(funded, claimed + (d_k / dt_h) * snap["hours_left"]) / funded, 2)
            if dt_h > 0 and funded else None)
        snap["px_chg_pct_since_prev"] = (
            round(100 * (core_px / float(prev["kntq_px_core_mid"]) - 1), 2)
            if core_px and prev.get("kntq_px_core_mid") else None)
    print(json.dumps(snap, indent=1))

    FIELDS = ["utc", "block", "unique_claimers", "claim_txs", "kntq_claimed", "usdc_paid", "kntq_funded",
              "pct_of_pool_claimed", "kntq_left_in_contract", "usdc_held_by_contract",
              "check_funded_minus_claimed_minus_left", "eligible_wallets", "pct_wallets_claimed",
              "kntq_px_core_mid", "kntq_px_evm_pool", "claim_price", "premium_vs_claim_pct", "hours_left",
              "rpc_calls_this_run", "since_prev_hours", "new_wallets", "new_kntq_claimed",
              "claim_pace_kntq_per_h", "projected_pct_at_deadline", "px_chg_pct_since_prev"]
    new = not os.path.exists(a.csv)
    with open(a.csv, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerow(snap)


if __name__ == "__main__":
    main()
