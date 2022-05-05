#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))
    count_arguments = 1
    while count_arguments != len(argv):
        print("{}: {:s}".format(count_arguments, str(argv[count_arguments])))
        count_arguments += 1
