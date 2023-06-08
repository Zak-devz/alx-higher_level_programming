#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    result = 0
    x = len(sys.argv) - 1
    for i in range(x):
        result += int(sys.argv[i + 1])
    print(result)
