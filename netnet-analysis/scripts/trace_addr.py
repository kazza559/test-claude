"""Fetch ERC20 Transfer logs (selected tokens) from/to an address into {symbol: {"out": [...], "in": [...]}}.

Usage: trace_addr.py ADDR OUT.json [start_block]

Single-address queries are allowed 10M-block spans on the official RPC (multi-address/wildcard only 30K),
so each token is queried on its own.
"""
import json, sys
from rpc import call, topic, get_logs, LOGS_RPC

TOKENS = {
    "0xca9c78dd337a67f6e0077f65f5e9218719d30edf": "NET", "0xb773ec2c326b7f98a5a83fc098825492f020a4c7": "sNET",
    "0x63c12667638f2ae6fc6ae09b43d98ec84a8586ea": "wsNET", "0x5fc5360d0400a0fd4f2af552add042d716f1d168": "USDG",
    "0xd0601ce157db5bdc3162bbac2a2c8af5320d9eec": "NVDA", "0x4a0e65a3eccec6dbe60ae065f2e7bb85fae35eea": "SPCX",
    "0xaf3d76f1834a1d425780943c99ea8a608f8a93f9": "AAPL", "0x2e0847e8910a9732eb3fb1bb4b70a580adad4fe3": "GOOGL",
    "0xe93237c50d904957cf27e7b1133b510c669c2e74": "MSFT", "0x6330d8c3178a418788df01a47479c0ce7ccf450b": "COIN",
    "0x0bd7d308f8e1639fab988df18a8011f41eacad73": "WETH", "0x117cc2133c37b721f49de2a7a74833232b3b4c0c": "SPY",
    "0x99347d5f70d3838763f6bddcf80304c8aa953b57": "nnUSDG", "0xbeeff033f34c046626b8d0a041844c5d1a5409dd": "MorphoVault",
}

if __name__ == "__main__":
    a = sys.argv[1].lower(); out = sys.argv[2]; start = int(sys.argv[3]) if len(sys.argv) > 3 else 10808643
    TR = topic("Transfer(address,address,uint256)")
    pad = "0x" + "0" * 24 + a[2:]
    n = int(call("eth_blockNumber", [], rpc=LOGS_RPC), 16)
    res = {}
    for t, sym in TOKENS.items():
        res[sym] = {"out": get_logs(t, [TR, pad], start, n, step=10_000_000), "in": get_logs(t, [TR, None, pad], start, n, step=10_000_000)}
        print(sym, len(res[sym]["out"]), len(res[sym]["in"]), flush=True)
    json.dump(res, open(out, "w"))
