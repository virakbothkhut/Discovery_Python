#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
    exit(0)

user_input = sys.argv[1]

















import sys


if len(sys.argv) != 2:
    print("none")
    exit(0)

input_str = sys.argv[1]

# Extract all occurrences of 'z'
z_chars = [char for char in input_str if char == 'z']

# Print result or "none" if no 'z' found
print("".join(z_chars) if z_chars else "none")
