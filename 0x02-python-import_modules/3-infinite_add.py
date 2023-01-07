#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    '''Program that adds up all its arguments'''
    count = len(sys.argv) - 1
    add = 0

    for i in range(1, (count + 1)):
        add += int(sys.argv[i])
    print("{}".format(add))
