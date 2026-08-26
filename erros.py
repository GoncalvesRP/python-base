#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to ASK Forgiveness than permission
# (É mais facil pedir perdao do que permissão)

try:
    names = open("names.txt").readlines() # FileNotFoundError
    1 / 1 # ZeroDivisionError
    print(names.append) # AttributeError
except FileNotFoundError:
    print("[Error] File names.txt not found")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You cant divide by zero!!!")
    sys.exit(1)
except AttributeError:
    print("[Error] List doesn´t have banana")
    sys.exit(1)

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
