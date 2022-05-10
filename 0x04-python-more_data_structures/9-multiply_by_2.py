#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for i in a_dictionary:
        mul = 2 * a_dictionary[i]
        new_dic[i] = mul
    return new_dic
