#!/usr/bin/env python3
import sys

param = sys.argv[1:]

if not param:
    print("none")
    exit(0)
print(f"Parameters:{len(sys.argv)-1}")
for p in param:
    print(f"{p}: {len(p)}")


