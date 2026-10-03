"""Fetch all Transfer logs of a token into JSONL (block, logIndex, tx, from, to, amount_raw). Resumable."""
import json, os, sys, time
from rpc import call, topic, LOGS_RPC
tok, out, start = sys.argv[1].lower(), sys.argv[2], int(sys.argv[3])
end = int(sys.argv[4]) if len(sys.argv) > 4 else int(call("eth_blockNumber", [], rpc=LOGS_RPC), 16)
TR = topic("Transfer(address,address,uint256)")
cur = start
if os.path.exists(out + ".cursor"):
    cur = int(open(out + ".cursor").read()) + 1
step = 300_000
f = open(out, "a")
t0 = time.time(); n = 0
while cur <= end:
    e = min(cur + step - 1, end)
    try:
        logs = call("eth_getLogs", [{"address": tok, "topics": [TR], "fromBlock": hex(cur), "toBlock": hex(e)}], rpc=LOGS_RPC, tries=3)
    except Exception as ex:
        msg = str(ex)
        if "exceeds limit" in msg or "timed out" in msg or "range" in msg:
            step = max(2000, step // 3); continue
        time.sleep(5); continue
    for l in logs:
        if len(l["topics"]) < 3: continue
        f.write(json.dumps([int(l["blockNumber"], 16), int(l["logIndex"], 16), l["transactionHash"], "0x" + l["topics"][1][-40:], "0x" + l["topics"][2][-40:], str(int(l["data"], 16) if l["data"] != "0x" else 0)]) + "\n")
    f.flush()
    open(out + ".cursor", "w").write(str(e))
    n += len(logs)
    print(f"{cur}-{e} step {step} got {len(logs)} total {n} elapsed {time.time()-t0:.0f}s", flush=True)
    cur = e + 1
    if len(logs) < 4000: step = min(3_000_000, int(step * 1.4))
    elif len(logs) > 8000: step = max(2000, int(step * 0.7))
print("DONE", n)
