#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list.copy()
    for i in new_list:
        new_list[3] = 9
        return new_list
