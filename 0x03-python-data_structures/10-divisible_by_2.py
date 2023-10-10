#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    divisable_list = []
    for idx in my_list:
        if (idx % 2) == 0:
            divisable_list.append(True)
        else:
            divisable_list.append(False)
        return divisible_list
