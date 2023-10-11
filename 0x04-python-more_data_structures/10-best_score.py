#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxValue = 0
    maxKey = None
    for key, n in a_dictionary.items():
        if n > maxValue:
            maxValue = n
            maxKey = key
    return maxKey
