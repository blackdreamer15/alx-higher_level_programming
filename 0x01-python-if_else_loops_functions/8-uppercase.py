#!/usr/bin/python3

def uppercase(str):
    for char in str:
        ascii_val = ord(char)

        if ascii_val > 96 and ascii_val < 123:
            scii_val = ascii_val - 32

        print(f"{chr(ascii_val)}", end="")
    print()
