#!/usr/bin/python3
def print_last_digit(num):
    if num > 0:
        last_digit = num % -(10)
        print(-(last_digit), end="")
    else:
        last_digit = num % 10
        print(last_digit, end="")
        return abs(last_digit)
