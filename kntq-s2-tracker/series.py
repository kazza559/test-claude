#!/usr/bin/env python3
"""Rebuild the hourly KNTQ Season-2 claim curve from Claimed() events (read-only eth_getLogs)."""
import json, sys, time, urllib.request, datetime as dt

CLAIM = "0x435bb7ea4eb481cb686606d089ea4dee4c6cc03b"
T_CLAIMED = "0x987d620f307ff6b94d58743cb7a7509f24071586a77759b77c2d4e29f75a2f9a"
DEPLOY = 47315563
RPCS = ["https://rpc.purroofgroup.com", "https://hyperliquid-rpc.publicnode.com", "https://rpc.hypurrscan.io"]

def post(url, payload, tries=4):
    d = json.dumps(payload).encode()
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=d, headers={"content-type": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            if i == tries - 1: raise
            time.sleep(2 * (i + 1))

def rpc(method, params, step_urls=RPCS):
    last = None
    for u in step_urls:
        try:
            r = post(u, {"jsonrpc": "2.0", "id": 1, "method": method, "params": params})
            if "error" in r: last = r["error"]; continue
            return r["result"]
        except Exception as e:
            last = e
    raise RuntimeError(f"{method} failed: {last}")

latest = int(rpc("eth_blockNumber", []), 16)
RANGE = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
logs, cur = [], DEPLOY
while cur <= latest:
    end = min(cur + RANGE - 1, latest)
    try:
        got = rpc("eth_getLogs", [{"address": CLAIM, "topics": [T_CLAIMED],
                                   "fromBlock": hex(cur), "toBlock": hex(end)}])
    except RuntimeError:
        half = (cur + end) // 2
        got = rpc("eth_getLogs", [{"address": CLAIM, "topics": [T_CLAIMED],
                                   "fromBlock": hex(cur), "toBlock": hex(half)}])
        got += rpc("eth_getLogs", [{"address": CLAIM, "topics": [T_CLAIMED],
                                    "fromBlock": hex(half + 1), "toBlock": hex(end)}])
    logs += got
    print(f"  {cur}-{end}: {len(got)} ({len(logs)} total)", file=sys.stderr)
    cur = end + 1

# block -> timestamp for the blocks we need (sample one block per 2000 to interpolate)
blocks = sorted({int(l["blockNumber"], 16) for l in logs})
anchors = {}
for b in sorted(set([blocks[0], blocks[-1], DEPLOY, latest] + blocks[::200])):
    ts = int(rpc("eth_getBlockByNumber", [hex(b), False])["timestamp"], 16)
    anchors[b] = ts
ab = sorted(anchors)
def t_of(b):
    import bisect
    i = bisect.bisect_left(ab, b)
    if i == 0: return anchors[ab[0]]
    if i >= len(ab): return anchors[ab[-1]]
    lo, hi = ab[i-1], ab[i]
    if hi == lo: return anchors[lo]
    f = (b - lo) / (hi - lo)
    return anchors[lo] + f * (anchors[hi] - anchors[lo])

rows, seen = {}, set()
for l in sorted(logs, key=lambda x: (int(x["blockNumber"], 16), int(x["logIndex"], 16))):
    b = int(l["blockNumber"], 16)
    who = "0x" + l["topics"][1][-40:]
    amt = int(l["data"][2:66], 16) / 1e18
    cost = int(l["data"][66:130], 16) / 1e6
    hour = dt.datetime.fromtimestamp(t_of(b), dt.timezone.utc).replace(minute=0, second=0, microsecond=0)
    k = hour.strftime("%Y-%m-%dT%H:00Z")
    r = rows.setdefault(k, {"claims": 0, "kntq": 0.0, "usdc": 0.0, "new_wallets": 0})
    r["claims"] += 1; r["kntq"] += amt; r["usdc"] += cost
    if who not in seen:
        seen.add(who); r["new_wallets"] += 1

out = {"generated_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
       "latest_block": latest, "total_claims": len(logs), "unique_wallets": len(seen),
       "total_kntq": round(sum(r["kntq"] for r in rows.values()), 2),
       "total_usdc": round(sum(r["usdc"] for r in rows.values()), 2),
       "hours": {k: {kk: (round(vv, 2) if isinstance(vv, float) else vv) for kk, vv in v.items()}
                 for k, v in sorted(rows.items())}}
json.dump(out, open("/home/user/test-claude/kntq-s2-tracker/claim_series.json", "w"), indent=1)
cum_k = cum_w = 0.0
print(f"{'hour (UTC)':18} {'claims':>7} {'new wal':>8} {'KNTQ':>12} {'cum KNTQ':>13} {'cum %':>7} {'cum wal':>8}")
for k, v in sorted(rows.items()):
    cum_k += v["kntq"]; cum_w += v["new_wallets"]
    print(f"{k:18} {v['claims']:7d} {v['new_wallets']:8d} {v['kntq']:12,.0f} {cum_k:13,.0f} {100*cum_k/5e7:6.2f}% {cum_w:8,.0f}")
