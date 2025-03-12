#!/usr/bin/env python3

try:
    num = 0
    while num <= 10:
        print(f"Table of {num}: ", end=" ")
        i  = 0
        while i <= 10:
            print((i * num), end=" ")
            i += 1
        print()
        num += 1
except ValueError:
    print("Error")