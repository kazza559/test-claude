import json, datetime, time, sys, os
from paths import DATA
from mc import multicall
NET="0xCA9c78Dd337A67F6e0077F65F5E9218719d30eDf"; SNET="0xb773ec2C326B7f98a5a83fc098825492F020a4c7"; STK="0xB078cc304A0B264C5F3680DC0488954ACcd02E87"
TR="0x04822Ea321A0DEE6F40656172F29312104855d66"; DIST="0x79e71F8a8a2912E40687a8820b2dC0fdd2f686b3"; ORA="0x929631b33F4070D6f54477fba3FD27566567dAca"
PT="0x650F58079dAa17ee28928c2F92d22291d038B2B0"; PAIR="0x59F95461E68e0c77605299791E1449f175165B54"; TEAM="0x3Bb7A23316f82C0e984fA2E784846d8928a35f42"
INV="0x92166e94Eea5B7799b761653881692f881dFC4C9"; PS="0x346e1a31171A0f7aC73909010b5435768d3B5462"; WS="0x63C12667638f2Ae6fC6ae09B43D98Ec84a8586eA"
BD="0xff32a969A0c567129eECD926D04657728E1980C1"; TC="0x086C58400b8708Ef993f256E12e752dcF0AC918e"; GB="0x575b7B7c97Ef3E21C82DAeB427899d583e1E913f"
U=["uint256"]
CALLS=[
 ("supply",NET,"totalSupply()",[],[],U),
 ("staked",STK,"totalStaked()",[],[],U),
 ("index",SNET,"index()",[],[],U),
 ("nav",TR,"backingPerToken()",[],[],U),
 ("rfv",TR,"rfv()",[],[],U),
 ("liquid",TR,"liquidUsdg()",[],[],U),
 ("morpho",TR,"morphoAssets()",[],[],U),
 ("pol",TR,"polRfv()",[],[],U),
 ("premium",DIST,"premium()",[],[],U),
 ("rate",DIST,"currentRateWad()",[],[],U),
 ("epochs",DIST,"epochsDistributed()",[],[],U),
 ("twap",ORA,"twapNetUsdg()",[],[],U),
 ("pteam_ex",PT,"exercised()",[],[],U),
 ("pteam_now",PT,"exercisableNow()",[],[],U),
 ("reserves",PAIR,"getReserves()",[],[],["uint112","uint112","uint32"]),
 ("team_net",NET,"balanceOf(address)",["address"],[TEAM],U),
 ("team_snet",SNET,"balanceOf(address)",["address"],[TEAM],U),
 ("team_ws",WS,"balanceOf(address)",["address"],[TEAM],U),
 ("tr_net",NET,"balanceOf(address)",["address"],[TR],U),
 ("inv_price",INV,"price()",[],[],U),
 ("inv_cap",INV,"capacityRemaining()",[],[],U),
 ("ps_active",PS,"active()",[],[],["bool"]),
 ("ws_supply",WS,"totalSupply()",[],[],U),
 ("pair_lp_supply",PAIR,"totalSupply()",[],[],U),
 ("tr_lp",PAIR,"balanceOf(address)",["address"],[TR],U),
 ("tc_pending",TC,"pendingNet()",[],[],U),
 ("gb_net",NET,"balanceOf(address)",["address"],[GB],U),
 ("bd_net",NET,"balanceOf(address)",["address"],[BD],U),
 ("inv_net",NET,"balanceOf(address)",["address"],[INV],U),
]
from blocktime import block_at as blk  # exact anchors; a linear 10 blocks/s fit drifts by hours

def snap(block):
    vals = multicall([(t,s,a,args,o) for (_,t,s,a,args,o) in CALLS], block)
    return {k: v for (k,*_), v in zip(CALLS, vals)}

def fmt(s):
    d={}
    E9=1e9; E18=1e18
    g=lambda k,sc: (s[k]/sc if s.get(k) is not None else None)
    d["supply"]=g("supply",E9); d["staked"]=g("staked",E9); d["index"]=g("index",E9)
    d["nav"]=g("nav",E18); d["rfv"]=g("rfv",E18); d["liquid"]=g("liquid",E18); d["morpho"]=g("morpho",E18); d["pol"]=g("pol",E18)
    d["premium"]=g("premium",E18); d["rate"]=g("rate",E18); d["epochs"]=s.get("epochs"); d["twap"]=g("twap",E18)
    d["pteam_ex"]=g("pteam_ex",E9); d["pteam_now"]=g("pteam_now",E9)
    r=s.get("reserves")
    if r: # netIsToken0 = False -> token0 USDG(6), token1 NET(9)
        d["pool_usdg"]=r[0]/1e6; d["pool_net"]=r[1]/1e9; d["spot"]=(r[0]/1e6)/(r[1]/1e9) if r[1] else None
    for k in ("team_net","team_snet","tr_net","tc_pending","gb_net","bd_net","inv_net"): d[k]=g(k,E9)
    d["team_ws"]=g("team_ws",E18); d["ws_supply"]=g("ws_supply",E18)
    d["inv_price"]=g("inv_price",E18); d["inv_cap"]=g("inv_cap",E18); d["ps_active"]=s.get("ps_active")
    d["tr_lp_share"]=(s["tr_lp"]/s["pair_lp_supply"]) if s.get("tr_lp") is not None and s.get("pair_lp_supply") else None
    return d

if __name__=="__main__":
    step_h = float(sys.argv[1]) if len(sys.argv)>1 else 24
    start = int(datetime.datetime(2026,7,17,tzinfo=datetime.timezone.utc).timestamp())
    end = int(time.time()) - 120
    out=[]
    ts=start
    while ts<=end:
        b=blk(ts)
        for i in range(5):
            try:
                s=fmt(snap(b)); break
            except Exception as e:
                time.sleep(3*(i+1)); s=None
        row={"ts":ts,"time":datetime.datetime.utcfromtimestamp(ts).isoformat(),"block":b, **(s or {})}
        out.append(row)
        print(row["time"], "nav", row.get("nav"), "spot", row.get("spot"), "prem", row.get("premium"), "supply", row.get("supply"), "staked", row.get("staked"), "pteam", row.get("pteam_ex"), flush=True)
        ts+=int(step_h*3600)
        time.sleep(0.3)
    # final: latest
    s=fmt(snap("latest")); out.append({"ts":int(time.time()),"time":"latest","block":"latest",**s})
    json.dump(out, open(sys.argv[2] if len(sys.argv)>2 else os.path.join(DATA, "history_12h.json"),"w"), indent=1)
