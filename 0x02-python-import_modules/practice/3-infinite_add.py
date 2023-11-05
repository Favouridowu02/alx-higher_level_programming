#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    r = 0
    for i in range(1, len(sys.argv)):
        r += int(sys.argv[i])
    print("{}".format(r))
