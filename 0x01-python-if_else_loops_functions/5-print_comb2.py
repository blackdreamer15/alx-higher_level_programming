#!/usr/bin/python3

for num in range(0, 100):
    if num < 10:
        print("0{0:d}".format(num), end=", ")
    else:
        if num == 99:
            print(f"{num:d}")
        else:
            print("{0:d}".format(num), end=", ")
