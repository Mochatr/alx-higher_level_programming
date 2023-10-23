#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Elements printed
    i = 0
    try:
        for i in x:
            print(my_list[i], end=" ")
            i += 1
    except IndexError:
        pass
    print()
    return i
