#!/usr/bin/python3
def print_lat_digit(number):
    """Print the last digit of a number and return it."""
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return (last_digit)
