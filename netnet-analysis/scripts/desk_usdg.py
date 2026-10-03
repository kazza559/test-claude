"""USDG paid into each bond desk and where it went (Treasury, router, other). Writes data/desk_usdg_flows.csv."""
import collections, csv, os
from rpc import call, get_logs, topic, LOGS_RPC
from paths import DATA

USDG = "0x5fc5360d0400a0fd4f2af552add042d716f1d168"
TREASURY = "0x04822ea321a0dee6f40656172f29312104855d66"
ROUTER = "0xc94135b63772b91d79d0a2daab2a8801f32359bd"  # USDG -> stock-token router used by every desk (likely Rialto)
DESKS = {
    "0x99b6ee6ede47d9a8a9bfd03f728a99b789df1961": "RwaDesk (listed)", "0xa84efc3136bf1bb89ade9e5be6ab32cb1a04f08d": "RwaDesk (unlisted 0xa84e)",
    "0x2f2f215b810fa692304cb0095804ab3c8e4cef78": "RwaDesk (unlisted 0x2f2f)", "0x70eaeec20c39df48509f1f3fab01f7dde207947b": "Desk (unlisted 0x70ea)",
    "0x732b3d1d3e8912cae75164fa14a6e1c4c64615b3": "Desk (unlisted 0x732b)",
}


def main():
    tr = topic("Transfer(address,address,uint256)")
    pad = lambda a: "0x" + "0" * 24 + a[2:]
    n = int(call("eth_blockNumber", [], rpc=LOGS_RPC), 16)
    rows = []
    for d, name in DESKS.items():
        out = get_logs(USDG, [tr, pad(d)], 10808643, n, step=10_000_000)
        inn = get_logs(USDG, [tr, None, pad(d)], 10808643, n, step=10_000_000)
        dest = collections.defaultdict(float)
        for l in out:
            dest["0x" + l["topics"][2][-40:]] += int(l["data"], 16) / 1e6
        usd_in = sum(int(l["data"], 16) for l in inn) / 1e6
        other = sum(v for k, v in dest.items() if k not in (TREASURY, ROUTER))
        rows.append([d, name, round(usd_in, 2), round(dest.get(TREASURY, 0), 2), round(dest.get(ROUTER, 0), 2), round(other, 2)])
        print(rows[-1], flush=True)
    with open(os.path.join(DATA, "desk_usdg_flows.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["desk", "name", "usdg_in", "to_treasury", "to_router_0xc941", "to_other"])
        w.writerows(rows)


if __name__ == "__main__":
    main()
