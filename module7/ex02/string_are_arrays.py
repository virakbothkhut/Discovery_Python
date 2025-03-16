#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
    exit(0)

text = sys.argv[1]
character_to_count = 'z'
count = sum(1 for char in text if char == character_to_count)
if count == 0:
    print("none")
else:
    print("z" * count, end="")
    print()











