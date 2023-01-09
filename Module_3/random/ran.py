##Write a Python program to read a random line from a file.


import random

line = random.choice(open('1.txt').readlines())
print(line)