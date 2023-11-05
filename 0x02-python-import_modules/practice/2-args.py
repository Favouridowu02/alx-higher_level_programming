#!/usr/bin/python3
if __name__ == "__main__":
    """prints the number of and the list of its arguments."""
    import sys
    if len(sys.argv) - 1 == 1:
        print("1 argument", end="")
    else:
        print("{:d} arguments".format(len(sys.argv) - 1), end="")
    if len(sys.argv) == 1:
        print(".")
    else:
        print(":")
    for j in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(j, sys.argv[j]))
