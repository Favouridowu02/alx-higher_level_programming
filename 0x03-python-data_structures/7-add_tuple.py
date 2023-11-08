#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """a function that adds 2 tuples.

    Arguments:
        tuple_a: the first tuple
        tuple_b: the second_tuple
    Return: tuple_sum
    """
    lenA = len(tuple_a)
    lenB = len(tuple_b)
# check for tuple_a
    if lenA < 1:
        tuple_a = (0, 0)
    elif lenA < 2:
        tuple_a = (tuple_a[0], 0)

# check for tuple_b
    if lenB < 1:
        tuple_b = (0, 0)
    elif lenB < 2:
        tuple_b = (tuple_b[0], 0)

    tuple_sum_0 = tuple_a[0] + tuple_b[0]
    tuple_sum_1 = tuple_a[1] + tuple_b[1]
    tuple_sum = tuple_sum_0, tuple_sum_1
    return tuple_sum
