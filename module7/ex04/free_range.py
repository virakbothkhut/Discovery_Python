#!/usr/bin/env python3

import sys
if (len(sys.argv) != 3):
    print("none")
    exit(0)

try:
    s = int(sys.argv[1])
    e = int(sys.argv[2])
except ValueError:
    print("none")
    exit(0)

if s <= e:
    arr = list(range(s, e+1))
else:
    # arr = list(range(e, s+1))
    # arr = list(range(s, e-1, -1))
    arr = list(range(e, s+1, 3))

print(arr)