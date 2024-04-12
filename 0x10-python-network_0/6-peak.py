#!/usr/bin/python3
"""
    This module contains a  function that finds a peak in a list of
    unsorted integers
"""

def find_peak(list_of_integers):
    """
        a function that finds a peak in a list of unsorted integers
    """
    peak = 0
    if len(list_of_integers) == 0:
        return None
    for i in list_of_integers:
        if peak < i:
            peak = i
    return peak 
