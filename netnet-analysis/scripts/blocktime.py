"""Block <-> timestamp mapping for Robinhood Chain from exact anchors (data/block_anchors.json).

Blocks come at ~9.87-9.98 per second and the rate drifts, so a single linear fit is off by hours after a few weeks;
piecewise-linear interpolation between binary-searched anchors keeps errors to seconds.
"""
import bisect, json, os
from paths import DATA

_A = json.load(open(os.path.join(DATA, "block_anchors.json")))
_B = [a[0] for a in _A]
_T = [a[1] for a in _A]


def _seg(i):
    i = min(max(i, 1), len(_B) - 1)
    return _B[i - 1], _T[i - 1], _B[i], _T[i]


def ts_of(block):
    b1, t1, b2, t2 = _seg(bisect.bisect_right(_B, block))
    return t1 + (block - b1) * (t2 - t1) / (b2 - b1)


def block_at(ts):
    b1, t1, b2, t2 = _seg(bisect.bisect_right(_T, ts))
    return int(b1 + (ts - t1) * (b2 - b1) / (t2 - t1))
