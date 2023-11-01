#!/usr/bin/python3
for n in range(9):
    for i in range(10):
        if n == 8 and i == 9:
            print(89)
            break
        if i > n:
            print("{}{}, ".format(n, i), end="")
