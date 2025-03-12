#!/usr/bin/env python3

try:
    number = int(input("Enter a number \n"))
    for i in range(10):
        print(f"{i} X {number} = {i * number}")    
except ValueError:
    print("Error")