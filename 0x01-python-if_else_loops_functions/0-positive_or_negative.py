#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is positive\n", end="")
elif number == 0:
    print(f"{number:d} is zero\n", end="")
elif number < 0:
    print(f"{number:d} is negative\n", end="")
