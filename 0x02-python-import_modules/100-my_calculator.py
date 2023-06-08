#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (operator == '-'):
        print("{} - {} = {}".format(a, b, calulator_1.sub(a, b)))
    elif (operator == '*'):
        print("{} * {} = {}".format(a, b, calulator_1.mul(a, b)))
    elif (operator == '/'):
        print("{} / {} = {}".format(a, b, calulator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
