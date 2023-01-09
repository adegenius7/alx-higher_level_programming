def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if my_list[i] < my_list[0]:
                my_list[0] = my_list[i]
            else:
                maximum = my_list[i]
            return maximum
