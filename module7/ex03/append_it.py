#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
    exit(0)

for p in sys.argv[1:]:
    if (p.endswith("ism")):
        continue
    else:
        print(p + "ism")