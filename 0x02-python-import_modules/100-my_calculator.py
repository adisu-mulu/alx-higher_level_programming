#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    if len(sys.argv) - 1 != 3:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]

        if operator == "+":
            print("{} + {} = {}".format(a, b, calc.add(a, b)))
        elif operator == "-":
            print("{} - {} = {}".format(a, b, calc.sub(a, b)))
        elif operator == "\*":
            print("{} * {} = {}".format(a, b, calc.mul(a, b)))
        elif operator == "/":
            print("{} / {} = {}".format(a, b, calc.div(a, b)))
        else:
            print("Unknown operator, Available operators: +, -, * and /")
            sys.exit(1)
