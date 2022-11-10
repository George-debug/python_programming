# 7) Write a function called process that receives a variable number of keyword arguments
# The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
# If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument and returning True/False) and will retain from the generated numbers only those for which the predicates are True.
# If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.
# If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list.
# The function will return the processed numbers.
# Example:
from typing import Callable
from itertools import islice


def sum_digits(x):
    return sum(map(int, str(x)))

# process(
#     filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
#     limit=2,
#     offset=2
# ) returns [34, 144]

# Explanation:
# Fibonacci sequence will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
# Valid numbers are: 2, 8, 34, 144, 610, 2584, 10946, 832040
# After offset: 34, 144, 610, 2584, 10946, 832040
# After limit: 34, 144


# overengineered? perhaps -_-
class FibonacciIterator:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 1000:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return self.a


def filter_all(filters: list[Callable[[int], bool]]) -> Callable[[int], bool]:
    def inner(x: int) -> bool:
        for f in filters:
            if not f(x):
                return False
        return True
    return inner


def process(**kwargs):
    fib = FibonacciIterator()
    if "filters" in kwargs:
        fib = filter(filter_all(kwargs["filters"]), fib)
    if "offset" in kwargs:
        for _ in range(kwargs["offset"]):
            next(fib)
    rv = []
    # tre sa citesc ce face islice, dar da, merge si asta
    if "limit" in kwargs:
        try:
            for _ in range(kwargs["limit"]):
                rv.append(next(fib))
        except StopIteration:
            pass

    return rv


rv = process(
    filters=[lambda item: item %
             2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2
)

print(rv)
