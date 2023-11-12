#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return

    big = my_list[0]
    for i in range(1, length):
        if big < my_list[i]:
            big = my_list[i]
    return big
