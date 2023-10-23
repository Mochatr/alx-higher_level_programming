#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Elements printed
    idx = 0
    try:
        while idx is not x:
            print(my_list[i], end="")
            i += 1
    except IndexError:
        None
    print()
    return idx
