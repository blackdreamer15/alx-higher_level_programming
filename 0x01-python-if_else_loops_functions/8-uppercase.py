#!/usr/bin/python3

def uppercase(str):
    for char in str:
        ascii_val = ord(char)

        if ascii_val > 96 and ascii_val < 123:
            ascii_val = ascii_val - 32

        print("{}".format(chr(ascii_val)), end="")
    print()
