# 1)
# a) Write a module named utils.py that contains one function called process_item.
# The function will have one parameter, x, and will return the least prime number greater than x. When run,
# the module will request an input from the user, convert it to a number and it will display the output of the process_item function.

import math


def is_prime(x: int) -> bool:
    if x == 2:
        return True
    if x % 2 == 0 or x <= 1:
        return False
    sqr = int(math.sqrt(x)) + 1
    for divisor in range(3, sqr, 2):
        if x % divisor == 0:
            return False
    return True


def process_item(x: int) -> int:
    x += 1
    while not is_prime(x):
        x += 1

    return x


# if the module is run as a script

if __name__ == '__main__':
    x = int(input('Enter a number: '))
    print(process_item(x))
