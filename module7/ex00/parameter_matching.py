#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
    exit(0)
    
user_enter = input("What was the parameter?: ")
the_word = sys.argv[1]

if user_enter == the_word:
    print("Good job!")
else:
    print("Nope, sorry..")



