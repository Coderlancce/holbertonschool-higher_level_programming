#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counterr = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            counterr += 1
        print("")
        return x
    except safe_print_list_error:
        print("")
        return counterr
