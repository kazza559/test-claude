import json, os
from paths import ABI
from eth_abi import encode, decode
from rpc import eth_call, sel
ABI_DIR = ABI

def load(name):
    return json.load(open(os.path.join(ABI_DIR, f"{name}.abi.json")))

def _type(o):
    if o["type"].startswith("tuple"):
        inner = ",".join(_type(c) for c in o["components"])
        return f"({inner})" + o["type"][5:]
    return o["type"]

def fn(abi, name, nin=None):
    for x in abi:
        if x.get("type") == "function" and x["name"] == name and (nin is None or len(x["inputs"]) == nin):
            return x
    raise KeyError(name)

def call(addr, abi, name, *args, block="latest"):
    f = fn(abi, name, len(args))
    ins = [_type(i) for i in f["inputs"]]
    outs = [_type(o) for o in f.get("outputs", [])]
    data = sel(f"{name}({','.join(ins)})") + (encode(ins, list(args)).hex() if ins else "")
    r = eth_call(addr, data, block)
    if r is None or r == "0x":
        return None
    v = decode(outs, bytes.fromhex(r[2:]))
    return v[0] if len(v) == 1 else v

def views(addr, abi, block="latest"):
    out = {}
    for x in abi:
        if x.get("type") == "function" and x.get("stateMutability") in ("view", "pure") and not x["inputs"]:
            try:
                out[x["name"]] = call(addr, abi, x["name"], block=block)
            except Exception as e:  # noqa
                out[x["name"]] = f"ERR {str(e)[:80]}"
    return out
