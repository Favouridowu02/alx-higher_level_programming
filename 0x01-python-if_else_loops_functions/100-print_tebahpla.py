#!/usr/bin/python3
for n in range(122, 96, -1):
    print("{}".format(chr(n - 32) if n % 2 else chr(n)), end="")
