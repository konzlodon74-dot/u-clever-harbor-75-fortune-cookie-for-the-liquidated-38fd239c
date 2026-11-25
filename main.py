#!/usr/bin/env python3
"""Fortune cookie for the liquidated crypto trader.

Writes a single fortune-cookie line to entry.txt.
"""

import os

FORTUNE = "Liquidated today, legend tomorrow: your portfolio hit zero, but your sense of humor just mooned \u2014 hold that."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
