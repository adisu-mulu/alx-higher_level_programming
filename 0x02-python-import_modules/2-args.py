#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} arguements:".format(len(sys.argv)-1))
    x = 0
    for arg in sys.argv[1:]:
        x += 1
        print("{}: {}".format(x, arg))

