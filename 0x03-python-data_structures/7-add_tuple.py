#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Initialize the variables that store the sum of elements from both tuples
    sumTuple_a = 0
    sumTuple_b = 0

    if len(tuple_a) > 0:
        sumTuple_a += tuple_a[0]

    if len(tuple_b) > 0:
        sumTuple_a += tuple_b[0]

    if len(tuple_a) > 1:
        sumTuple_b += tuple_a[1]

    if len(tuple_b) > 1:
        sumTuple_b += tuple_b[1]

    result = (sumTuple_a, sumTuple_b)

    return result
