#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for item in matrix:
        for col in range(len(item)):
            if col < len(item) - 1:
                print("{:d}".format(item[col]), end=" ")
            else:
                print("{:d}".format(item[col]))
