#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for element in my_list[:x]:
            try:
                element = int(element)
                print("{:d}".format(element), end=" ")
                i += 1
            except (TypeError, ValueError):
                None
        print()
    except (IndexError, TypeError):
        None
    return i
