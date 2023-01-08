#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    lists = my_list[::-1]
    for x in lists:
        print("{:d}".format(x))
