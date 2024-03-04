#!/usr/bin/python3
"""
    This Module is a technical session, I am ready to debug the task a hand,
    It contains a function that returns a list of  lists of integers representing
    the pascal triangle of n
"""

def pascal_triangle(n):
    """
        a Function that returns a list of lists of integers representing
        the Pascal’s triangle of n
    """
    total = []
    prev = []

    for i in range(1, n):
        if i == 1:
            prev = [1]
            total.append([1])

        current = [1]
        for b in range(0, len(prev) - 1):
            current.append(prev[b] + prev[b + 1])
        current.append(1)
        total.append(current)
        prev = current
    return total
