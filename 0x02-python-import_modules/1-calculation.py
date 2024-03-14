#!/usr/bin/python3
if __name__ == "__main_":
    import calculator_1 as calc
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} + {} = {}".format(a, b, calc.sub(a, b)))
    print("{} + {} = {}".format(a, b, calc.mul(a, b)))
    print("{} + {} = {}".format(a, b, calc.div(a, b)))
