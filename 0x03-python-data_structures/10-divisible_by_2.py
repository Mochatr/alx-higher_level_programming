#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    are_multiples = []
    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            are_multiples.append(True)
        else:
            are_multiples.append(False)
    return (are_multiples)
