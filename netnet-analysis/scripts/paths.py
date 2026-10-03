"""Folder layout: data/ (small committed outputs), raw/ (large log dumps, git-ignored), abi/ (verified ABIs from Sourcify)."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
RAW = os.path.join(ROOT, "raw")
ABI = os.path.join(ROOT, "abi")
for _d in (DATA, RAW):
    os.makedirs(_d, exist_ok=True)
