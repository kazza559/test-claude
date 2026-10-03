"""Call HoodScan MCP tools (public, read-only) over Streamable HTTP JSON-RPC."""
import json, re, sys, time, requests
URL = "https://hoodscan.co/mcp"
H = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
_id = 0

def tool(name, **args):
    global _id
    _id += 1
    for i in range(4):
        r = requests.post(URL, headers=H, json={"jsonrpc": "2.0", "id": _id, "method": "tools/call", "params": {"name": name, "arguments": args}}, timeout=90)
        if r.status_code == 429:
            time.sleep(int(r.headers.get("Retry-After", 5)) + 1); continue
        t = r.text
        m = re.findall(r"^data: (.*)$", t, re.M)
        d = json.loads(m[-1]) if m else json.loads(t)
        if "error" in d:
            raise RuntimeError(d["error"])
        res = d["result"]
        if res.get("structuredContent"):
            return res["structuredContent"]
        txt = "".join(c.get("text", "") for c in res.get("content", []) if c.get("type") == "text")
        try:
            return json.loads(txt)
        except Exception:
            return txt
    raise RuntimeError("rate limited")

if __name__ == "__main__":
    name = sys.argv[1]
    args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    out = tool(name, **args)
    print(json.dumps(out, indent=1) if not isinstance(out, str) else out)
