#!/usr/bin/python3
for num in range(0, 10):
    for num2 in range(num+1, 10):
        digit = str(num) + str(num2)
        if num < 8:
            print("{}".format(digit), end=", ")
        else:
            print("{}".format(digit))
