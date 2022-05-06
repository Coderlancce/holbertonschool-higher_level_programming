#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit 1

    a = int(argv[2])
    b = int(argv[4])

    if argv[3] == '+':
        print("{} + {} = {}".format(argv[2], argv[4], add(a, b)))
    elif argv[3] == '-':
        print("{} - {} = {}".format(argv[2], argv[4], sub(a, b)))
    elif argv[3] == '*':
         print("{} * {} = {}".format(argv[2], argv[4], mul(a, b)))
    elif argv [3] == '/':
         print("{} / {} = {}".format(argv[2], argv[4], div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit 1
