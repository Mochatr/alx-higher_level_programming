#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None

    maxValue = my_list[0]
    for n in my_list:
        if n > maxValue:
            maxValue = n

    return maxValue
