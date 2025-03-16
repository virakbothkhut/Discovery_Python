#!/usr/bin/env python3
import sys

def downcase_it(text):
    return text.lower()
if (len(sys.argv) < 2):
    print("none")
    exit(0)
else:
    for p in sys.argv[1:]:
        print(downcase_it(p))