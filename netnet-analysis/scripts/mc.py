"""Multicall3 batching over archive-capable RPC (drpc free plan supports historical eth_call)."""
from eth_abi import encode, decode
from rpc import call, sel
MC3 = "0xcA11bde05977b3631167028862bE2a173976CA11"
ARCHIVE = "https://robinhood.drpc.org"

def multicall(calls, block="latest", rpc=ARCHIVE):
    """calls: list of (target, sig, argtypes, args, outtypes). Returns list of decoded values or None."""
    payload = []
    for tgt, sig, at, args, ot in calls:
        data = bytes.fromhex(sel(sig)[2:]) + (encode(at, args) if at else b"")
        payload.append((tgt, data))
    data = sel("tryAggregate(bool,(address,bytes)[])") + encode(["bool", "(address,bytes)[]"], [False, payload]).hex()
    blk = block if isinstance(block, str) else hex(block)
    r = call("eth_call", [{"to": MC3, "data": data}, blk], rpc=rpc)
    res = decode(["(bool,bytes)[]"], bytes.fromhex(r[2:]))[0]
    out = []
    for (ok, rd), (tgt, sig, at, args, ot) in zip(res, calls):
        if not ok or len(rd) == 0:
            out.append(None); continue
        try:
            v = decode(ot, rd)
            out.append(v[0] if len(v) == 1 else v)
        except Exception:
            out.append(None)
    return out
