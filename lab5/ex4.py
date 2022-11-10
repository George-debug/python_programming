# 4) Write a function that receives a variable number of arguments and keyword arguments.
# The function returns a list containing only the arguments which are dictionaries,
# containing minimum 2 keys and at least one string key with minimum 3 characters.

# Example:

# my_function(
#  {1: 2, 3: 4, 5: 6},
#  {'a': 5, 'b': 7, 'c': 'e'},
#  {2: 3},
#  [1, 2, 3],
#  {'abc': 4, 'def': 5},
#  3764,
#  dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
#  test={1: 1, 'test': True}
# ) will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]

def dictionary_is_ok(dictionary: dict) -> bool:
    # "minimum 2 keys"
    if len(dictionary) < 2:
        return False
    # "at least one string key with minimum 3 characters"
    for key in dictionary:
        if isinstance(key, str) and len(key) >= 3:
            return True
    return False


def my_function(*args, **kwargs):
    all = list(args) + list(kwargs.values())
    return [x for x in all if isinstance(x, dict) and dictionary_is_ok(x)]


# a doua functie "my_function"
print(my_function(
    {1: 2, 3: 4, 5: 6},
    {'a': 5, 'b': 7, 'c': 'e'},
    {2: 3},
    [1, 2, 3],
    {'abc': 4, 'def': 5},
    3764,
    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    test={1: 1, 'test': True}
))
