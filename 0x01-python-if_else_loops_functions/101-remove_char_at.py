#!/usr/bin/python3
def remove_char_at(str, n):
    nstr = ""
    for a, b in enumerate(str):
        if a != n:
            nstr += b
        return nstr
