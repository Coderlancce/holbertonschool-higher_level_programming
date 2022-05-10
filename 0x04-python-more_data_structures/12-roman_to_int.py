#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string and type(roman_string) is str:
        convert = 0
        for i in range(len(roman_string)):
            if i > 0 and roman_dict[roman_string[i]] > roman_dict[roman_string[i - 1]]:
                convert += dict[roman_string[i] - 2 * dict[roman_string[i - 1]
            else:
                convert += dict[roman_string[i]]
        return conver
    return (0)
