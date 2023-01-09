#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for cell in matrix:
            for x in cell:
                print("{:d}".format(x))
