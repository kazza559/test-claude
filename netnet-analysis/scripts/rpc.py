"""Minimal JSON-RPC helpers for Robinhood Chain (chainId 4663)."""
import json, time, itertools, requests
from Crypto.Hash import keccak

RPCS = ["https://rpc.mainnet.chain.robinhood.com", "https://robinhood-rpc.publicnode.com", "https://robinhood.drpc.org"]
_rr = itertools.cycle(range(len(RPCS)))
S = requests.Session()

def k256(b):
    h = keccak.new(digest_bits=256); h.update(b if isinstance(b, bytes) else b.encode()); return h.hexdigest()

def sel(sig):
    return "0x" + k256(sig)[:8]

def topic(sig):
    return "0x" + k256(sig)

def call(method, params, tries=6, rpc=None):
    last = None
    for i in range(tries):
        url = rpc or RPCS[next(_rr)]
        try:
            r = S.post(url, json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params}, timeout=60)
            if r.status_code == 429:
                last = "http 429"; time.sleep(2 * (i + 1)); continue
            d = r.json()
            if "error" in d:
                last = d["error"]
                msg = json.dumps(d["error"]).lower()
                if "429" in msg or "too many requests" in msg or "rate" in msg:
                    time.sleep(2 * (i + 1)); continue
                if any(x in msg for x in ("block range", "range", "limit exceeded", "too many results", "exceed", "10000", "response size", "query returned", "max results")):
                    raise OverflowError(d["error"])
                if "execution reverted" in msg or "revert" in msg:
                    return None
                time.sleep(1 + i)
                continue
            return d["result"]
        except OverflowError:
            raise
        except Exception as e:  # noqa
            last = e
            time.sleep(1 + i)
    raise RuntimeError(f"{method} failed: {last}")

def eth_call(to, data, block="latest"):
    return call("eth_call", [{"to": to, "data": data}, block])

def addr_arg(a):
    return a.lower().replace("0x", "").rjust(64, "0")

def u(x):
    return int(x, 16) if x and x != "0x" else None

def as_addr(x):
    return ("0x" + x[-40:]) if x and len(x) >= 42 else None

def as_str(x):
    if not x or x == "0x": return None
    b = bytes.fromhex(x[2:])
    try:
        if len(b) >= 64:
            off = int.from_bytes(b[:32], "big"); ln = int.from_bytes(b[off:off+32], "big")
            return b[off+32:off+32+ln].decode(errors="replace")
        return b.rstrip(b"\0").decode(errors="replace")
    except Exception:
        return x

def block_number():
    return int(call("eth_blockNumber", []), 16)

def block_ts(n):
    b = call("eth_getBlockByNumber", [hex(n), False])
    return int(b["timestamp"], 16)

LOGS_RPC = "https://rpc.mainnet.chain.robinhood.com"

def get_logs(address, topics, frm, to, step=2_000_000, min_step=200, verbose=False, max_step=10_000_000):
    """Fetch logs with adaptive range splitting (official RPC allows <=10M-block spans)."""
    out = []
    cur = frm
    while cur <= to:
        end = min(cur + step - 1, to)
        try:
            q = {"topics": topics, "fromBlock": hex(cur), "toBlock": hex(end)}
            if address: q["address"] = address
            res = call("eth_getLogs", [q], rpc=LOGS_RPC)
            out.extend(res)
            if verbose: print(f"  {cur}-{end}: {len(res)} (step {step})", flush=True)
            cur = end + 1
            if len(res) < 3000 and step < max_step: step = min(max_step, int(step * 1.6))
        except (OverflowError, RuntimeError) as e:
            if step <= min_step: raise
            step = max(min_step, step // 4)
            if verbose: print(f"  shrink to {step}: {str(e)[:120]}", flush=True)
    return out
