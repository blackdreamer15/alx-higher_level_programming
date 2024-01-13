#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        if not item:
            return None

        for col in range(len(item)):
            if col < len(item) - 1:
                print("{:d}".format(item[col]), end=" ")
            else:
                print("{:d}".format(item[col]))
