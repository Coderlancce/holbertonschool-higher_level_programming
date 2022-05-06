#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = 0
    elements = 1
    while elements != len(argv):
        number += int(argv[elements])
        elements += 1
    print("{}".format(number))
