#!/usr/bin/python3
"""
    This module contains a  function that finds a peak in a list of
    unsorted integers
"""

def find_peak(list_of_integers):
    """
        a function that finds a peak in a list of unsorted integers
    """
    if len(list_of_integers) == 0 or list_of_integers == []:
        return None
    
    length = len(list_of_integers)
    mid = int(length // 2)

    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid + 1] and\
            list_of_integers[mid] >= list_of_integers[mid - 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
