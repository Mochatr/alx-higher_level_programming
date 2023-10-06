#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    """ Count """
    c = len(sys.argv) - 1
    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count))
    for n in range(c):
        print("{:d}: {:d}".format(n + 1, sys.argv[n + 1]))
