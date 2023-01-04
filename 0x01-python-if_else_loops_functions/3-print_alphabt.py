#!/usr/bin/python3
start = 97
stop = 123
while start in range(start, stop):
    if start != 101 and start != 113:
        print("{:c}".format(start), end="")
    start += 1
