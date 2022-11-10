# 3) Using functions, anonymous functions, list comprehensions and filter,
# implement three methods to generate a list with all the vowels in a given string.

# For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].

def variant_1(string: str) -> list:
    return [x for x in string if x in 'aeiou']


def variant_2(string: str) -> list:
    filtered = filter(lambda x: x in 'aeiou', string)

    return list(filtered)


def variant_3(string: str) -> list:
    rv = []

    for x in string:
        if x in 'aeiou':
            rv.append(x)

    return rv


test = 'Programming in Python is fun'

print(variant_1(test))
print(variant_2(test))
print(variant_3(test))
