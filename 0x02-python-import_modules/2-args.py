#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    i = len(argv)

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} arguments:".format(i))
    else:
        print("{} arguments:".format(i))

    if i != 0:
        i = 1
        for arg in sys.argv:
            print("{}: {}".format(i, arg))
            i += 1
