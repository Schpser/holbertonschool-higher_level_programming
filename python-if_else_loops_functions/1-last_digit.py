#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
str_1 = "and is greater than 5"
str_2 = "and is 0"
str_3 = "and is less than 6 and not 0"

last_digit = abs(number) % 10 if number >= 0 else -(-number % 10)

print(f"{str} {number} is {last_digit}", end=" ")
if last_digit > 5:
    print(str_1)
elif last_digit == 0:
    print(str_2)
else:
    print(str_3)
