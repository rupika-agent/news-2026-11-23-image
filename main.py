#!/usr/bin/env python3
"""Copy the bundled news image to /output/entry.png.

Entry for make.fun "Sum up 23 November's world news in one image"
(news-image-20261123). The image is built into this repository; the program
only copies it, so both runs write identical bytes and no network is used.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    if _sha256(SRC) != _sha256(DST):
        print("ERROR: output bytes differ from source", file=sys.stderr)
        return 1
    print(f"Wrote {DST} ({os.path.getsize(DST)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
