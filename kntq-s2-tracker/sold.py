#!/usr/bin/env python3
"""Did S2 claimers sell? (a) KNTQ bridged EVM->HyperCore per hour, (b) top claimers' remaining balance."""
import json, urllib.request, datetime as dt, time, sys
KNTQ="0x000000000000780555bd0bca3791f89f9542c2d6"; BRIDGE="0x200000000000000000000000000000000000007c"
T_TRANSFER="0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
RPC="https://rpc.purroofgroup.com"
def post(url,p,tries=4):
    for i in range(tries):
        try:
            r=urllib.request.Request(url,data=json.dumps(p).encode(),headers={"content-type":"application/json"})
            with urllib.request.urlopen(r,timeout=90) as f: return json.loads(f.read().decode())
        except Exception as e:
            if i==tries-1: raise
            time.sleep(2*(i+1))
def rpc(m,p): 
    r=post(RPC,{"jsonrpc":"2.0","id":1,"method":m,"params":p})
    if "error" in r: raise RuntimeError(r["error"])
    return r["result"]
latest=int(rpc("eth_blockNumber",[]),16)
START=47290000  # ~1 day before the claim window, for a baseline
logs=[];cur=START
while cur<=latest:
    end=min(cur+9999,latest)
    logs+=rpc("eth_getLogs",[{"address":KNTQ,"topics":[T_TRANSFER,None,"0x"+BRIDGE[2:].rjust(64,"0")],
                              "fromBlock":hex(cur),"toBlock":hex(end)}])
    print(f"  {cur}-{end}  {len(logs)} bridge-in transfers",file=sys.stderr); cur=end+1
# timestamps: sample anchors
blocks=sorted({int(l["blockNumber"],16) for l in logs})
anch={}
for b in sorted(set([START,latest]+blocks[::60]+[blocks[-1]] if blocks else [START,latest])):
    anch[b]=int(rpc("eth_getBlockByNumber",[hex(b),False])["timestamp"],16)
ab=sorted(anch)
import bisect
def t_of(b):
    i=bisect.bisect_left(ab,b)
    if i==0: return anch[ab[0]]
    if i>=len(ab): return anch[ab[-1]]
    lo,hi=ab[i-1],ab[i]
    return anch[lo] if hi==lo else anch[lo]+(b-lo)/(hi-lo)*(anch[hi]-anch[lo])
rows={}
for l in logs:
    b=int(l["blockNumber"],16); amt=int(l["data"][2:66],16)/1e18
    frm="0x"+l["topics"][1][-40:]
    k=dt.datetime.fromtimestamp(t_of(b),dt.timezone.utc).strftime("%Y-%m-%dT%H:00Z")
    r=rows.setdefault(k,{"n":0,"kntq":0.0,"senders":set()})
    r["n"]+=1; r["kntq"]+=amt; r["senders"].add(frm)
print(f"\n{'hour (UTC)':18} {'transfers':>9} {'senders':>8} {'KNTQ -> HyperCore':>18}")
for k,v in sorted(rows.items()):
    print(f"{k:18} {v['n']:9d} {len(v['senders']):8d} {v['kntq']:18,.0f}")
json.dump({k:{"n":v["n"],"kntq":round(v["kntq"],2),"senders":len(v["senders"])} for k,v in sorted(rows.items())},
          open("bridge_in_hourly.json","w"),indent=1)
# ---- top claimers: how much do they still hold on HyperEVM?
st=json.load(open("state.json"))
top=sorted(((a,v[0]/1e18) for a,v in st["wallets"].items()),key=lambda x:-x[1])[:100]
batch=[{"jsonrpc":"2.0","id":i,"method":"eth_call",
        "params":[{"to":KNTQ,"data":"0x70a08231"+a[2:].rjust(64,"0")},"latest"]} for i,(a,_) in enumerate(top)]
res={r["id"]:int(r.get("result","0x0"),16)/1e18 for r in post(RPC,batch)}
core=json.loads(urllib.request.urlopen(urllib.request.Request("https://api.hypurrscan.io/holders/KNTQ",
      headers={"user-agent":"kntq-tracker"}),timeout=60).read().decode())
corebal={}
it=core.items() if isinstance(core,dict) else ((x[0],x[1]) for x in core)
for a,v in it: corebal[a.lower()]=float(v)/1e8 if float(v)>1e12 else float(v)
claimed=sum(x[1] for x in top); held_evm=sum(res.values())
held_core=sum(corebal.get(a.lower(),0) for a,_ in top)
print(f"\nTop 100 claimers: claimed {claimed:,.0f} KNTQ")
print(f"  still on HyperEVM {held_evm:,.0f}   on HyperCore {held_core:,.0f}   total {held_evm+held_core:,.0f}")
print(f"  => at most {100*(held_evm+held_core)/claimed:.1f}% of what they claimed is still in those wallets")
print(f"\n{'wallet':44}{'claimed':>12}{'evm now':>12}{'core now':>12}{'kept %':>8}")
for i,(a,c) in enumerate(top[:25]):
    h=res.get(i,0); cb=corebal.get(a.lower(),0)
    print(f"{a:44}{c:12,.0f}{h:12,.0f}{cb:12,.0f}{100*(h+cb)/c:7.0f}%")
