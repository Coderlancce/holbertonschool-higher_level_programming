#!/usr/bin/python3
def max_integer(my_list=[]):
    maxim_number = 0
    for i in range(len(my_list)):
        if my_list[i] < maxim_number:
            continue
        else:
            maxim_number = my_list[i]
    return maxim_number
