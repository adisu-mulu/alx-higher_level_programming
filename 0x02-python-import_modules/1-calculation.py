#!/usr/bin/python3
if __name__ == "__main_":
    import 1-calculation
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, 1-calculation.add(a, b)))
    print("{} + {} = {}".format(a, b, 1-calculation.sub(a, b)))
    print("{} + {} = {}".format(a, b, 1-calculation.mul(a, b)))
    print("{} + {} = {}".format(a, b, 1-calculation.div(a, b)))
