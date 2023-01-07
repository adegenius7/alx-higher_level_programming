#!/usr/bin/python3
if __name__ == '__main__':
    '''counting the number of args '''
    import sys
    arg = sys.argv
    length = len(arg) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("1: {}".format(arg[1]), end='\n')
    else:
        print("{} arguments:".format(length))
    for i in range(length):
        print("{}: {}".format(i + 1, arg[i + 1]), end='\n')
