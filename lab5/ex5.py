# 5) Write a function with one parameter which represents a list.
# The function will return a new list containing all the numbers found in the given list.

# Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]

def is_number(x):
    # isinstance(bool, int) = True, deci asa
    return isinstance(x, (int, float, complex)) and not isinstance(x, bool)

# a treia functie "my_function"


def my_function(list: list) -> list:
    return [x for x in list if is_number(x)]


print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
