#!/usr/bin/python3
def remove_char_at(str, n):
    res = ""
    for i in range(len(str)):
        if i == n:
            continue
        res += str[i]
    return res
