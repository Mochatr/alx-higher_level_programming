#!/usr/bin/python3
def magic_string():
    magic_string.counter = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string_counter)])
