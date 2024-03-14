#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 1:
        print("{} arguement:".format(len(sys.argv) - 1))
        x = 0
        for arg in sys.argv[1:]:
            x += 1
            print("{}: {}".format(x, arg))

    elif len(sys.argv) - 1 == 0:
        print("{} arguements.".format(len(sys.argv)-1))
    else:
        print("{} arguements:".format(len(sys.argv)-1))
        x = 0
        for arg in sys.argv[1:]:
            x += 1
            print("{}: {}".format(x, arg))

