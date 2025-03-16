#!/usr/bin/env python3

import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    while (len(string) < 8):
        string += 'Z'
    print(string)

if len(sys.argv) < 2:
    print("none")
    exit(0)
    
for x in sys.argv[1:]:
    if len(x) > 8:
        shrink(x)
    elif len(x) < 8:
        enlarge(x)
    else:
        print(x)