#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
language that combines remarkable power with very clear syntax"
str = "object-oriented programming with " + str[str.index("Python"):].split()[0]
print(str)
