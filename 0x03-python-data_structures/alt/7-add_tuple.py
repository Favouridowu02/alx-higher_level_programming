#!/usr/bin/python3
def add_tuple(tuple_a, tuple_b):
    """A function that adds two tuples element-wise.

    Arguments:
        tuple_a: the first tuple
        tuple_b: the second tuple
    Return: tuple_sum
    """
    # Ensure that both tuples have at least 2 elements
    tuple_a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a
    tuple_b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b

    # Calculate the element-wise sum
    tuple_sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_sum
