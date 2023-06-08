#!/usr/bin/python3
from sys import argv
x = len(argv) - 1
if x == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(x))
for i in range(1, x + 1):
        print("{}: {}".format(i, argv[i]))
