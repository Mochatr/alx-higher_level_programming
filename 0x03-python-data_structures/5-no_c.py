#!/usr/bin/python3
def no_c(my_string):
    # Modified string
    result_str = ""
    for idx in range(len(my_string)):
        if (my_string[idx] != 'c' and my_string[idx] != 'C'):
            result_str += my_string[idx]
    return result_str
