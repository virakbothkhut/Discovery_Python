#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
    exit(0)
keyword = sys.argv[1]
words = sys.argv[2]

check = re.findall(keyword, words)
if check:
    print(len(check))
else:
    print("none")







