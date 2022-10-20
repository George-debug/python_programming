# 1. Write a function to return a list of the first n numbers in the Fibonacci string.

def first_n_fibonacci(n: int) -> list[int]:
    if n == 0:
        return []
    elif n == 1:
        return [1]
    a = 1
    b = 1

    rv = [a, b]

    for i in range(n - 2):
        a, b = b, a + b
        rv.append(b)

    return rv

# print(first_n_fibonacci(10))


# =================================================================================================
# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0:
            return False

    return True

def get_prime_numbers(numbers: list[int]) -> list[int]:
    rv = []
    for n in numbers:
        if is_prime(n):
            rv.append(n)
    return rv

# print(get_prime_numbers(list(range(100))))


# =================================================================================================
# 3. Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)

def get_all_sets(a: list[int], b: list[int]) -> (list[int], list[int], list[int], list[int]):
    a_set = set(a)
    b_set = set(b)

    return (a_set & b_set, a_set | b_set, a_set - b_set, b_set - a_set)

# print(get_all_sets([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))


# =================================================================================================
# 4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer).
# The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]

def compose(notes: list[str], moves: list[int], start: int) -> list[str]:
    rv = []
    for move in moves:
        rv.append(notes[start])
        start += move
        start %= len(notes)
    return rv + [notes[start]]

# print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


# =================================================================================================
# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).

def matrix_for_print(matrix: list[list[int]]) -> str:
    rv = "[\n"
    for line in matrix:
        rv += "    " + str(line) + ",\n"
    rv += "]"
    return rv
        

def replace_under_main_diagonal(matrix: list[list[int]]) -> list[list[int]]:
    rv = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[i])):
            if i > j:
                line.append(0)
            else:
                line.append(matrix[i][j])
        rv.append(line)
    return rv

# print(matrix_for_print(replace_under_main_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))


# =================================================================================================

# 6. Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.

def get_x_times_in_lists(x: int, *lists: list) -> list:
    counter = {}

    for l in lists:
        for item in l:
            if item in counter:
                counter[item] += 1
            else:
                counter[item] = 1
    
    return [item for item in counter if counter[item] == x]

# print(get_x_times_in_lists(2, [1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))


# =================================================================================================
# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.

def is_palindrom(n: int) -> bool:
    m = 0

    while n:
        m = m * 10 + n % 10
        n //= 10

        if m == n or m == n // 10:
            return True

    return False

def get_palindroms(numbers: list[int]) -> (int, int):
    palindroms = [n for n in numbers if is_palindrom(n)]
    return (len(palindroms), max(palindroms))


# print(get_palindroms(range(10, 1000, 3)))


# =================================================================================================
# 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
# For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
# otherwise it should contain characters that have the ASCII code not divisible by x.
# Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must return list of lists.

def get_charactes_by_x(text: str, x: int, flag: bool):
    rv = []
    for c in text:
        if flag and ord(c) % x == 0:
            rv.append(c)
        elif not flag and ord(c) % x != 0:
            rv.append(c)
    return rv

def get_divisible_by_x_list(strings: list[str], x:int = 1, flag:bool = True) -> list[list[str]]:
    return [get_charactes_by_x(s, x, flag) for s in strings]

# print(get_divisible_by_x_list(["test", "hello", "lab002"], 2, False))


# =================================================================================================
# 9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list of tuples (line, column)
# each one representing a seat of a spectator which can't see the game. A spectator can't see the game if there is at least one taller spectator standing in front of him.
# All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.
# Example:
# FIELD

# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 7, 2],
# [5, 5, 2, 5, 6, 4],
# [6, 6, 7, 6, 7, 5]] 

# Will return : [(2, 2), (3, 4), (2, 4)] 

def get_coordonates_of_not_visible_seats(matrix: list[list[int]]) -> list[(int, int)]:
    rv = []
    
    for i in range(1, len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < matrix[i - 1][j]:
                rv.append((i, j))

    return rv

# print(get_coordonates_of_not_visible_seats([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))


# =================================================================================================
# Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains the first items in the lists,
# the second element contains the items on the position 2 in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 
# Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to generate max ([len(x) for x in input_lists]) tuples.

def get_same_position(*lists: list) -> list[tuple]:
    rv = []
    max_len = max([len(x) for x in lists])

    for i in range(max_len):
        tup = []

        for l in lists:
            if i < len(l):
                tup.append(l[i])
            else:
                tup.append(None)

        rv.append(tuple(tup))
    
    return rv

# print(get_same_position([1,2,3], [5,6,7], ["a", "b", "c"]))


# =================================================================================================
# 11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def order_by_third_char(tuples: list[tuple]) -> list[tuple]:
    return sorted(tuples, key=lambda x: x[1][2])

# print(order_by_third_char([('abc', 'bcd'), ('abc', 'zza')]))


# =================================================================================================
# 12. Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme.
# Two words rhyme if both of them end with the same 2 letters.
# Example:
# group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']] 

def group_by_rhyme(words: list[str]) -> list[list[str]]:
    rv = {}

    for w in words:
        last_2_chars = w[-2:]
        if last_2_chars in rv:
            rv[last_2_chars].append(w)
        else:
            rv[last_2_chars] = [w]

    return [rv[k] for k in rv]

# print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))