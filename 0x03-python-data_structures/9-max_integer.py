def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        my_list.sort()
        new_list = my_list
    return new_list[-1]
