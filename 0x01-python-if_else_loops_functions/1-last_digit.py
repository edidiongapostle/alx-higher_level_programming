#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst = abs(number) % 10
if number >= 0:
    if lst > 5:
        print(f'Last digit of {number} is {lst} and is greater than 5')
    if lst == 0:
        print(f'Last digit of {number} is {lst} and is 0')
    if lst < 6 and not lst == 0:
        print(f'Last digit of {number} is {lst} and is less than 6 and not 0')
elif number < 0:
    lst = -lst
    print(f'Last digit of {number} is {lst} and is less than 6 and not 0')
