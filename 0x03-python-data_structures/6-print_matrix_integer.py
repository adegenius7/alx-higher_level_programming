#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for columns in row:
            if columns == row[-1]:
                print("{:d}".format(columns), end='')
            else:
                print("{:d}".format(columns), end=' ')
        print()
