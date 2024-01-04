#!/usr/bin/python3

for num in range(0, 100):
    if num < 10:
        print(f"0{num:d}", end=", ")
    else:
        if num == 99:
            print(f"{num:d}")
        else:
            print(f"{num:d}", end=", ")
