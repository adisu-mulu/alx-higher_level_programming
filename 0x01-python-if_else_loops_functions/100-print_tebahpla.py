#!/usr/bin/python3
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    if i == 0:
        print(chr(c).lower(), end="")
    else:
        print(chr(c).upper(), end="")
        i = 32 - i
