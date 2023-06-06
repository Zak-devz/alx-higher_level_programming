#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 or ord(c) < 123:
        print("{} is lower".format(c))
        return True
    else:
        print("{} is upper".format(c))
        return False

