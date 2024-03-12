#!/usr/bin/python3
for num in range(0, 100):
    if num < 10:
        strnum = "0" + str(num)
    else:
        strnum = str(num)
    if num < 99:
        print("{}".format(strnum), end=", ")
    else:
        print("{}".format(strnum))
