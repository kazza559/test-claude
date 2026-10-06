"""Extend data/block_anchors.json with exact (block, timestamp) pairs: one per UTC midnight since the last anchor, plus the head."""
import datetime, json, os
from rpc import call
from paths import DATA

R = "https://robinhood.drpc.org"
FN = os.path.join(DATA, "block_anchors.json")


def bts(n):
    return int(call("eth_getBlockByNumber", [hex(n), False], rpc=R)["timestamp"], 16)


def block_at(ts, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if bts(mid) < ts:
            lo = mid + 1
        else:
            hi = mid
    return lo


def main():
    anchors = dict(tuple(a) for a in json.load(open(FN)))
    head = int(call("eth_blockNumber", [], rpc=R), 16)
    head_ts = bts(head)
    # drop the previous head anchor if it is not a midnight one; it is re-added below
    last_b = max(b for b, t in anchors.items() if t % 86400 == 0)
    day = anchors[last_b] + 86400
    while day < head_ts:
        b = block_at(day, last_b, head)
        anchors[b] = bts(b)
        last_b = b
        day += 86400
    anchors[head] = head_ts
    out = sorted(anchors.items())
    json.dump(out, open(FN, "w"))
    for b, t in out[-6:]:
        print(b, datetime.datetime.utcfromtimestamp(t))


if __name__ == "__main__":
    main()
