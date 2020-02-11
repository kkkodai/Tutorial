import re

with open("ensyu1.txt", "r") as f:
    line = f.readline()
    while line:
        print(re.findall('[0-9]+',line))
        line = f.readline()

with open("ensyu2.txt", "r") as f:
    line = f.readline()
    while line:
        print(re.findall('[-]?[[0-9]+.]*[0-9]+',line))
        line = f.readline()

with open("ensyu3.txt", "r") as f:
    line = f.readline()
    while line:
        print(re.findall('[a-zA-Z]+',line))
        line = f.readline()
