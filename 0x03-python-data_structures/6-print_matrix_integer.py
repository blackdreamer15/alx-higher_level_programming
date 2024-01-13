#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for item in matrix:
        for col in range(len(item)):
            print("{:d}".format(item[col]), end="")

            if col < len(item) - 1:
                print(" ", end="")
                continue

        print()
