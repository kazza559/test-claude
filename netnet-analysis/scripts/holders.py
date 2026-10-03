"""Current holders of NET in every form: NET balance + sNET balance + wsNET balance x index.

NET and wsNET balances are rebuilt from transfer logs (raw/*.jsonl); sNET is rebasing, so balances are read
on chain (multicall) for every address that ever received sNET.
Writes raw/holders.json and data/holders_top100.csv.
"""
import collections, csv, json, os
from mc import multicall
from flows import label
from paths import DATA, RAW

ZERO = "0x0000000000000000000000000000000000000000"
SNET = "0xb773ec2c326b7f98a5a83fc098825492f020a4c7"


def balances(fn, dec):
    b = collections.defaultdict(int)
    for line in open(os.path.join(RAW, fn)):
        _, _, _, fr, to, amt = json.loads(line)
        amt = int(amt)
        if fr != ZERO:
            b[fr] -= amt
        if to != ZERO:
            b[to] += amt
    return {a: v / 10 ** dec for a, v in b.items() if v > 0}


def main():
    netb = balances("net_transfers.jsonl", 9)
    wsb = balances("wsnet_transfers.jsonl", 18)
    cand = sorted({json.loads(l)[4] for l in open(os.path.join(RAW, "snet_transfers.jsonl"))} - {ZERO})
    snb = {}
    for i in range(0, len(cand), 400):
        chunk = cand[i:i + 400]
        res = multicall([(SNET, "balanceOf(address)", ["address"], [a], ["uint256"]) for a in chunk], "latest")
        snb.update({a: r / 1e9 for a, r in zip(chunk, res) if r})
    idx = multicall([(SNET, "index()", [], [], ["uint256"])], "latest")[0] / 1e9
    tot = collections.defaultdict(lambda: [0.0, 0.0, 0.0])
    for a, v in netb.items():
        tot[a][0] += v
    for a, v in snb.items():
        tot[a][1] += v
    for a, v in wsb.items():
        tot[a][2] += v
    rows = sorted(((a, n, s, w, n + s + w * idx, label(a) or "") for a, (n, s, w) in tot.items()), key=lambda r: -r[4])
    # Staking holds the non-circulating sNET supply (OHM v1 layout); it is not a holder
    rows = [r for r in rows if r[5] != "Staking"]
    json.dump(rows, open(os.path.join(RAW, "holders.json"), "w"))
    with open(os.path.join(DATA, "holders_top100.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["address", "net", "snet", "wsnet", "net_equivalent", "label"])
        for r in rows[:100]:
            w.writerow([r[0], round(r[1], 4), round(r[2], 4), round(r[3], 4), round(r[4], 4), r[5]])
    users = [r for r in rows if not r[5] or r[5] in ("TeamSafe", "RWASleeve")]
    ueq = sum(r[4] for r in users)
    print("index", idx, "user-held NET-eq", round(ueq, 1), "holders", sum(1 for r in users if r[4] > 0.001))
    for n in (1, 10, 100):
        print(f"top{n} share {sum(r[4] for r in users[:n]) / ueq * 100:.1f}%")


if __name__ == "__main__":
    main()
