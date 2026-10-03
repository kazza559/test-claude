"""Classify every NET / sNET / wsNET transfer by transaction into protocol and market flows.

Per transaction, each address gets a NET-equivalent delta: dNET + dsNET + dwsNET * index(t).
Pools, protocol contracts and known routers are separated from end users; what remains are
wallets (EOAs, Safes, bots). Output: daily flow table and per-wallet aggregates (7d / 30d / all).
"""
import bisect, collections, datetime, json, os, sys
from paths import DATA, RAW

D = DATA
ZERO = "0x0000000000000000000000000000000000000000"
from blocktime import ts_of


# ---------- address sets ----------
PROTO = {
    "0xb078cc304a0b264c5f3680dc0488954accd02e87": "Staking", "0x04822ea321a0dee6f40656172f29312104855d66": "Treasury",
    "0x79e71f8a8a2912e40687a8820b2dc0fdd2f686b3": "Distributor", "0xff32a969a0c567129eecd926d04657728e1980c1": "BondDepository",
    "0x92166e94eea5b7799b761653881692f881dfc4c9": "InverseBond", "0x346e1a31171a0f7ac73909010b5435768d3b5462": "PremiumSeller",
    "0x086c58400b8708ef993f256e12e752dcf0ac918e": "TaxCollector", "0x650f58079daa17ee28928c2f92d22291d038b2b0": "pTEAM",
    "0x575b7b7c97ef3e21c82daeb427899d583e1e913f": "GenesisBond", "0xb773ec2c326b7f98a5a83fc098825492f020a4c7": "sNET",
    "0x63c12667638f2ae6fc6ae09b43d98ec84a8586ea": "wsNET", "0xa1ee052ec32532304a7522bd9a4b594ec28ff1b1": "Zap",
    "0x4638617808e3f1cf237c0d33ae818126d5c77e17": "TurboRouter", "0x9d53d5e3bd5e8d4cbfa6db1ca238aea02e651010": "MorphoBlue",
    "0x99b6ee6ede47d9a8a9bfd03f728a99b789df1961": "RwaDesk", "0xa84efc3136bf1bb89ade9e5be6ab32cb1a04f08d": "RwaDesk(prev)",
    "0x2f2f215b810fa692304cb0095804ab3c8e4cef78": "RwaDesk(v1)", "0x70eaeec20c39df48509f1f3fab01f7dde207947b": "Desk-0x70ea",
    "0x732b3d1d3e8912cae75164fa14a6e1c4c64615b3": "Desk-0x732b", "0x8154e35166f21305adac82f95b54de8acd44d23a": "Desk-0x8154",
    "0x7cf28d61d42352eb2fd68167e9b08f73cbbf21eb": "PackDesk", "0x7332b329860986e596b2fd71e9c53786c0242ce5": "PrizeVault",
    "0x823b016b546178c4c47a830b92333ad44e655d06": "BonusBook", "0xcc4a7c03a2d4d248b8da0e35c178944799feac70": "DrawController",
    "0x21089cfcdbf47902a2f3950200ce9ea66bf79ee4": "ClimbDesk", "0xf125ad8abde2591609a982e0b6a51309fdf7db37": "JackpotPool",
    "0xa99d15dace9aede816600a31c3e4158926000f3c": "CoinFlipDesk", "0x75edfe49d9ec8c23a9931c5ef32ec56b2444a141": "SpacexInvaders",
    "0xf56e517652bb18e519871abb13a382d205f6e375": "FlightSimDesk", "0x757122439420900ca44a80c390d586011fd72c8a": "TurboDesk",
    "0x712f52fd42d7b89fd444e0cc4430020faa9cfb26": "BlackjackDesk", "0xe109eaf5fa12f93168947f62cc340c96f4dc15eb": "BoardroomDesk",
    "0xa8d5c34aef923d73ae9161ea934eb27a2219e416": "BasketsDesk", "0x7ef9528408d99f98056922291048f0710001e015": "PredictDesk",
    "0xb488368902b1cbd7533f1536c3f860065398d3e9": "HouseVault", "0x3174de69a84c53f82f6b6dca5c64e705cffe8dd6": "TheBook",
    "0xc866e4f53f1439d85171a06395ce37b887d16fa1": "BookZap", "0x99347d5f70d3838763f6bddcf80304c8aa953b57": "nnUSDG",
    "0xf6ec124ca62c841384abd0e128552cf9eb446205": "FuturesCH", "0x3a7dce19447f9028c360592fdfdb3f27c50dae29": "UnderwritingVault",
    "0xd1604dcadb949a28c7cfa8cd044641b8c520ef3f": "FuturesCH2", "0x38f620aec20b116ad19629e8f91842d0d4ed8c39": "UnderwritingVault2",
    "0x212dbb2af8f150c6d66bc78910775fa8f52d5785": "Desk-0x212d",
}
TEAM = {"0x3bb7a23316f82c0e984fa2e784846d8928a35f42": "TeamSafe", "0x498752d5fa0600cbd613074c151abe15b3fec7cb": "RWASleeve"}
POOL_EXTRA = {
    "0x8366a39cc670b4001a1121b8f6a443a643e40951": "UniV4 PoolManager", "0x00000000000014aa86c5d3c41765bb24e11bd701": "Ekubo",
    "0x2bf75792cbd40cc494101fc8772141823ec43949": "v3 pool 2%", "0x3b46b4f0036a718329aa25bf1238392527a0800b": "Ramses DLMM",
    "0xbabed015d6f4b4bbb8cdbda530dd443bd369ff50": "Abyss", "0x01eee4a5bf66cad762393a493fcf46ea9f5b0b92": "pool 0x01ee",
    "0x2283688c7f3562b8e2ba5395a41dff31c5c94fa9": "RobinSwap v2", "0x3d862596a58688470ba38d3452ff0337abcf4eb3": "UniV2 NET/WETH",
    "0x64b5d51dcd053199b89db33d43acaea91833cfae": "v2 E280/NET", "0x6655975143ac17544fe9b1406da2dab448df5b9b": "v2 NET/HorseMeat",
    "0x5c890e2537bc43428d3ede9715eec17200db36fb": "v2 PACK/NET", "0x4d7dccf061e6f7f8ac74bf5cd823115c017f1580": "v2 CHEF/NET",
    "0x571b47509023e42e8ff8e3207158057306c0e0e4": "v2 GOOD/NET", "0xe4832f6b2f9f8a97bcfa2fe31c92ab4c07ff8948": "v2 PACK/NET 2",
}
ROUTERS = {  # pass-through contracts (net out within a tx); listed so leftovers are not read as end users
    "0x39b38686a19836ac10162c490e4558e120cbbe5f": "0x Settler", "0x6aa80dbbed9ae5ab45fbf61f9644fada3b29326e": "0x Settler",
    "0x1d4b86491ec211257cbedd77a4380a7494624eff": "0x Settler", "0x6aea160407e73658c6c546de727a7ef4cd73a1ad": "0x SettlerIntent",
    "0xb92fe925dc43a0ecde6c8b1a2709c170ec4fff4f": "Relay", "0xb477751b76cf82d00a686a1232f5fcd772414af3": "LiFi",
    "0x09ad820aac5779683b481c4674208a4e1b024afa": "DexAggregatorCore", "0x542298e710b32b49883577883b75b39ef18883ce": "V4UtilsRouter",
    "0xcb3d2a42022741b06f9b38459e3dd1ee9a64d129": "V4UtilsRouter", "0x3a7f029e3ad003ab5aa78ccf101b1b543eaed6f9": "Executor",
    "0x20f6ee51340adeed01a59b0e65cb3703f3dc860c": "DexAggregator", "0x8876789976decbfcbbbe364623c63652db8c0904": "UniversalRouter",
    "0xb9b207a77c84556eb6e02d2c0e7873bcf4e9c8d5": "KyberSwap", "0x36dc95f1f088e11c0066dc19173f745655002bc2": "V4Adapter",
    "0x99b4dcc3a6fe2eee7dccb932248916a533be0989": "UniversalRouter2", "0xa8281d411b9ad6bc3ba3fde6d4b1631fcafda45d": "SwapRouter",
    "0x888888888889758f76e7103c6cbf23abbf58f946": "PendleRouter", "0xb300000b72deaeb607a12d5f54773d1c19c7028d": "Diamond",
    "0x89e5db8b5aa49aa85ac63f691524311aeb649eba": "UniV2Router", "0x111116053f09d34a7eae8102887004445176ca11": "Router 0x1111",
    "0xb55ba9617dafae1236313c3cb7806439ceefbd13": "SimpleSettlement",
}


def load_pools():
    pools = dict(POOL_EXTRA)
    try:
        for p in json.load(open(os.path.join(D, "ds_token.json")))["pairs"]:
            if len(p["pairAddress"]) == 42:
                pools[p["pairAddress"].lower()] = f"{p['dexId']} {p['baseToken']['symbol']}/{p['quoteToken']['symbol']}"
    except Exception:
        pass
    try:
        for a, v in json.load(open(os.path.join(D, "gt_pools_all.json"))).items():
            if len(a) == 42:
                pools.setdefault(a, f"{v['dex']} {v['name']}")
    except Exception:
        pass
    return pools


POOLS = load_pools()
CANON = "0x59f95461e68e0c77605299791e1449f175165b54"


def label(a):
    return PROTO.get(a) or TEAM.get(a) or POOLS.get(a) or ROUTERS.get(a)


# ---------- price + index series ----------
def price_series():
    c = json.load(open(os.path.join(D, "gt_ohlcv_4h.json")))["data"]["attributes"]["ohlcv_list"]
    c.sort()
    return [x[0] for x in c], [x[4] for x in c]


PT, PP = price_series()


def px(t):
    i = bisect.bisect_right(PT, t) - 1
    return PP[max(i, 0)]


H = [r for r in json.load(open(os.path.join(D, "history_12h.json"))) if r["time"] != "latest" and r.get("index")]
HT = [r["ts"] for r in H]
HI = [r["index"] for r in H]


def index_at(t):
    i = bisect.bisect_right(HT, t) - 1
    return HI[max(i, 0)] if HT else 1.0


def read(fn, dec, kind):
    with open(os.path.join(RAW, fn)) as f:
        for line in f:
            b, li, tx, fr, to, amt = json.loads(line)
            yield b, li, tx, fr, to, int(amt) / 10 ** dec, kind


def by_tx():
    """Merge the three sorted streams into per-tx lists (files are block-ordered)."""
    import heapq
    streams = [read("net_transfers.jsonl", 9, "NET"), read("snet_transfers.jsonl", 9, "sNET"), read("wsnet_transfers.jsonl", 18, "wsNET")]
    cur_tx, cur = None, []
    for rec in heapq.merge(*streams, key=lambda r: (r[0], r[1])):
        if rec[2] != cur_tx:
            if cur:
                yield cur_tx, cur
            cur_tx, cur = rec[2], []
        cur.append(rec)
    if cur:
        yield cur_tx, cur


def main():
    now = max(PT) + 4 * 3600
    t7, t30 = now - 7 * 86400, now - 30 * 86400
    day = collections.defaultdict(lambda: collections.defaultdict(float))
    wallet = collections.defaultdict(lambda: collections.defaultdict(float))
    mint_src = collections.defaultdict(float)
    ntx = 0
    for tx, recs in by_tx():
        ntx += 1
        b = recs[0][0]
        t = ts_of(b)
        p = px(t)
        idx = index_at(t)
        dk = datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d")
        net = collections.defaultdict(float)   # raw NET deltas
        eq = collections.defaultdict(float)    # NET-equivalent deltas (NET + sNET + wsNET*index)
        minted_to = collections.defaultdict(float)
        for (_, _, _, fr, to, amt, kind) in recs:
            mult = 1.0 if kind != "wsNET" else idx
            if kind == "NET":
                if fr == ZERO:
                    minted_to[to] += amt
                net[fr] -= amt; net[to] += amt
            eq[fr] -= amt * mult; eq[to] += amt * mult
        # --- supply events
        for to, amt in minted_to.items():
            src = {"0xb078cc304a0b264c5f3680dc0488954accd02e87": "mint_rebase", "0xff32a969a0c567129eecd926d04657728e1980c1": "mint_bond",
                   "0x3bb7a23316f82c0e984fa2e784846d8928a35f42": "mint_pteam", "0x346e1a31171a0f7ac73909010b5435768d3b5462": "mint_premium",
                   "0x575b7b7c97ef3e21c82daeb427899d583e1e913f": "mint_genesis"}.get(to, "mint_other")
            day[dk][src] += amt
            mint_src[src] += amt
        if net.get(ZERO, 0) > 0:
            day[dk]["burn"] += net[ZERO]
        # --- pool flows (NET only; pools hold NET, never sNET)
        pool_d = {a: v for a, v in net.items() if a in POOLS and abs(v) > 1e-9}
        pool_out = -sum(v for v in pool_d.values() if v < 0)   # NET leaving pools (bought)
        pool_in = sum(v for v in pool_d.values() if v > 0)     # NET entering pools (sold)
        # internal arbitrage between pools nets out; count gross for volume
        day[dk]["pool_out"] += pool_out
        day[dk]["pool_in"] += pool_in
        day[dk]["pool_out_usd"] += pool_out * p
        day[dk]["pool_in_usd"] += pool_in * p
        if CANON in pool_d:
            day[dk]["canon_net_in"] += pool_d[CANON]
        # premium seller / tax conversion sells into canonical pool
        if net.get("0x346e1a31171a0f7ac73909010b5435768d3b5462", 0) < 0 and pool_in > 0:
            day[dk]["premium_sell"] += min(pool_in, -net["0x346e1a31171a0f7ac73909010b5435768d3b5462"] + minted_to.get("0x346e1a31171a0f7ac73909010b5435768d3b5462", 0))
        if net.get("0x086c58400b8708ef993f256e12e752dcf0ac918e", 0) < -1e-9 and pool_in > 0:
            day[dk]["tax_sell"] += -net["0x086c58400b8708ef993f256e12e752dcf0ac918e"]
        if net.get("0x086c58400b8708ef993f256e12e752dcf0ac918e", 0) > 0:
            day[dk]["tax_in"] += net["0x086c58400b8708ef993f256e12e752dcf0ac918e"]
        # staking flows (NET into/out of Staking, excluding rebase mints)
        sd = net.get("0xb078cc304a0b264c5f3680dc0488954accd02e87", 0) - minted_to.get("0xb078cc304a0b264c5f3680dc0488954accd02e87", 0)
        if sd > 0:
            day[dk]["stake"] += sd
        elif sd < 0:
            day[dk]["unstake"] += -sd
        # bonds: NET paid out of BondDepository (claims), desks paid out to subscribers
        bd = net.get("0xff32a969a0c567129eecd926d04657728e1980c1", 0) - minted_to.get("0xff32a969a0c567129eecd926d04657728e1980c1", 0)
        if bd < 0:
            day[dk]["bond_claim"] += -bd
        for desk in ("0x99b6ee6ede47d9a8a9bfd03f728a99b789df1961", "0xa84efc3136bf1bb89ade9e5be6ab32cb1a04f08d", "0x2f2f215b810fa692304cb0095804ab3c8e4cef78", "0x70eaeec20c39df48509f1f3fab01f7dde207947b", "0x732b3d1d3e8912cae75164fa14a6e1c4c64615b3"):
            dd = net.get(desk, 0)
            if dd < 0:
                day[dk]["desk_claim"] += -dd
            elif dd > 0:
                day[dk]["desk_fill"] += dd
        ib = net.get("0x92166e94eea5b7799b761653881692f881dfc4c9", 0)
        if ib > 0:
            day[dk]["inverse_bond"] += ib
        # --- wallets (end users): NET-equivalent deltas
        users = {a: v for a, v in eq.items() if a != ZERO and not label(a) and abs(v) > 1e-9}
        team_d = {a: v for a, v in eq.items() if a in TEAM and abs(v) > 1e-9}
        traded = pool_out + pool_in > 1e-9
        for a, v in list(users.items()) + list(team_d.items()):
            w = wallet[a]
            if traded:
                key = "buy" if v > 0 else "sell"
            elif minted_to.get(a):
                key = "mint"
            else:
                srcs = {label(x) for x, vv in eq.items() if x != a and abs(vv) > 1e-9}
                if v > 0 and ("BondDepository" in srcs or any(s and "Desk" in s for s in srcs)):
                    key = "bondclaim"
                elif v < 0 and "InverseBond" in srcs:
                    key = "sell_floor"
                else:
                    key = "xfer_in" if v > 0 else "xfer_out"
            usd = abs(v) * p
            w[key] += abs(v); w[key + "_usd"] += usd
            if t >= t30:
                w[key + "_30"] += abs(v); w[key + "_usd30"] += usd
            if t >= t7:
                w[key + "_7"] += abs(v); w[key + "_usd7"] += usd
            w["n"] += 1
            w["last"] = max(w["last"], t)
            if not w.get("first"):
                w["first"] = t
            if traded:
                day[dk]["users_buy" if v > 0 else "users_sell"] += abs(v)
                day[dk]["users_buy_usd" if v > 0 else "users_sell_usd"] += usd
                day[dk]["buyers" if v > 0 else "sellers"] += 1
    out = {"days": {k: dict(v) for k, v in sorted(day.items())}, "wallets": {k: dict(v) for k, v in wallet.items()}, "mint_src": mint_src, "ntx": ntx, "now": now}
    json.dump(out, open(os.path.join(RAW, "flows.json"), "w"))
    print("txs", ntx, "wallets", len(wallet))
    print("mints", {k: round(v, 1) for k, v in mint_src.items()})


if __name__ == "__main__":
    main()
