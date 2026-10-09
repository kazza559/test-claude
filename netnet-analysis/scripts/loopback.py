"""Loopback: the Morpho Blue market that lends USDG against wsNET (NetNet's own lending market).

Reads the market, its oracle (LoopbackOracle: clamp(TWAP x 0.9, NAV, 5 x NAV) x index, floored at NAV) and the
adaptive-curve borrow rate, then every borrower's position (from SupplyCollateral logs) to build a liquidation
ladder: how much collateral becomes liquidatable as the oracle's NET price falls.

Writes data/loopback_summary.json and data/loopback_positions.json.
"""
import json, math, os
from mc import multicall
from rpc import get_logs, topic, block_number
from paths import DATA

MORPHO = "0x9d53d5e3bd5e8d4cbfa6db1ca238aea02e651010"
MID = "0xaa586d26a6fe62d9c0f0948fede6e2130500ac7a655587447e2d4a37e6330589"
WSNET = "0x63c12667638f2ae6fc6ae09b43d98ec84a8586ea"
SNET = "0xb773ec2c326b7f98a5a83fc098825492f020a4c7"
SLEEVE = "0x498752d5fa0600cbd613074c151abe15b3fec7cb"
MP = ["(address,address,address,address,uint256)"]
MK = ["(uint128,uint128,uint128,uint128,uint128,uint128)"]


def main():
    b = bytes.fromhex(MID[2:])
    params, mk, idx = multicall([(MORPHO, "idToMarketParams(bytes32)", ["bytes32"], [b], ["address", "address", "address", "address", "uint256"]),
                                 (MORPHO, "market(bytes32)", ["bytes32"], [b], ["uint128"] * 6),
                                 (SNET, "index()", [], [], ["uint256"])])
    index = idx / 1e9
    oracle, irm, lltv = params[2], params[3], params[4] / 1e18
    px, rate, coll_total = multicall([(oracle, "price()", [], [], ["uint256"]),
                                      (irm, "borrowRateView(" + MP[0] + "," + MK[0] + ")", MP + MK, [params, mk], ["uint256"]),
                                      (WSNET, "balanceOf(address)", ["address"], [MORPHO], ["uint256"])])
    ws_px = px / 1e24                     # USDG per wsNET (Morpho scale 1e36, 18-dec collateral, 6-dec loan)
    net_px = ws_px / index                # credited NET price
    apr = rate / 1e18 * 365 * 86400
    supply, borrow = mk[0] / 1e6, mk[2] / 1e6

    logs = get_logs(MORPHO, [topic("SupplyCollateral(bytes32,address,address,uint256)"), MID], 10808643, block_number())
    users = sorted({"0x" + lg["topics"][3][-40:] for lg in logs})
    pos = []
    for k in range(0, len(users), 100):
        pos += multicall([(MORPHO, "position(bytes32,address)", ["bytes32", "address"], [b, u], ["uint256", "uint128", "uint128"]) for u in users[k:k + 100]])
    rows = []
    for u, p in zip(users, pos):
        if not p:
            continue
        coll, debt = p[2] / 1e18, (p[1] * mk[2] / mk[3] / 1e6 if mk[3] else 0)
        if debt < 1:  # dust or collateral-only
            continue
        rows.append({"user": u, "coll_wsnet": coll, "debt_usdg": debt, "ltv": debt / (coll * ws_px), "liq_net_px": debt / (coll * lltv) / index})
    rows.sort(key=lambda r: -r["liq_net_px"])
    ladder = []
    for x in (190, 180, 170, 160, 150, 140, 130, 120, 100):
        hit = [r for r in rows if r["liq_net_px"] >= x]
        ladder.append({"net_px": x, "positions": len(hit), "collateral_net_eq": round(sum(r["coll_wsnet"] for r in hit) * index, 1),
                       "debt_usdg": round(sum(r["debt_usdg"] for r in hit))})
    sl = next((r for r in rows if r["user"] == SLEEVE), None)
    out = {"market_id": MID, "oracle": oracle, "lltv": lltv, "supply_usdg": supply, "borrow_usdg": borrow, "util_pct": borrow / supply * 100,
           "borrow_apr_pct": apr * 100, "borrow_apy_pct": (math.exp(apr) - 1) * 100, "oracle_wsnet_usd": ws_px, "oracle_net_usd": net_px, "index": index,
           "collateral_wsnet": coll_total / 1e18, "collateral_net_eq": coll_total / 1e18 * index, "borrowers": len(rows), "users_ever": len(users),
           "aggregate_ltv": borrow / (coll_total / 1e18 * ws_px), "ladder": ladder, "sleeve": sl}
    json.dump(out, open(os.path.join(DATA, "loopback_summary.json"), "w"), indent=1)
    json.dump(rows, open(os.path.join(DATA, "loopback_positions.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "ladder"}, indent=1))
    for r in ladder:
        print(r)


if __name__ == "__main__":
    main()
