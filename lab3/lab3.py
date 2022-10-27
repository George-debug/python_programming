
# 1. Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)
def get_weird_sets(a: list[int], b: list[int]):
    a_set = set(a)
    b_set = set(b)

    return (a_set & b_set, a_set | b_set, a_set - b_set, b_set - a_set)

# print(get_weird_sets([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))


# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters
# in the character string and the values are the number of occurrences of that character in the given text.

# Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
# {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .

def string_to_dict(text: str) -> dict[str, int]:
    rv = {}
    for c in text:
        if c in rv:
            rv[c] += 1
        else:
            rv[c] = 1
    return rv


# print(string_to_dict("Ana has apples"))


# 3. Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be recursively
# covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

def compare_sets(a: set, b: set) -> bool:
    if len(a) != len(b):
        return False

    for i in a:
        if i not in b:
            return False

    return True


def compare_lists(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if type(a[i]) != type(b[i]):
            return False
        if type(a[i]) == dict:
            if not compare_dictionaries(a[i], b[i]):
                return False
        elif type(a[i]) == list:
            if not compare_lists(a[i], b[i]):
                return False
        elif type(a[i]) == set:
            if not compare_sets(a[i], b[i]):
                return False
        else:
            if a[i] != b[i]:
                return False

    return True


def compare_dictionaries(a: dict, b: dict) -> bool:
    if len(a) != len(b):
        return False

    for k in a:
        if k not in b:
            return False
        if type(a[k]) != type(b[k]):
            return False
        if type(a[k]) == dict:
            if not compare_dictionaries(a[k], b[k]):
                return False
        elif type(a[k]) == list:
            if not compare_lists(a[k], b[k]):
                return False
        elif type(a[k]) == set:
            if not compare_sets(a[k], b[k]):
                return False
        else:
            if a[k] != b[k]:
                return False

    return True


# my_dictionary = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# my_dictionary2 = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# my_list1 = [1, 2, 3]
# my_list2 = [1, 2, 5]

# my_set1 = {1, 2, 3}
# my_set2 = {1, 2, 5}

# for key in my_dictionary:
#     print(key)

# for key in my_list:
#     print(key)

# for key in my_set:
#     print(key)

# print(compare_dictionaries({
#     "a": 1,
#     "b": 2,
#     "c": [1, 2, {"a": 1, "b": {1, 2, 3}, "c": 3}],
# }, {
#     "a": 1,
#     "b": 2,
#     "c": [1, 2, {"a": 1, "b": {1, 3, 3}, "c": 3}],
# }))


# 4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters.
# Build and return a string that represents the corresponding XML element. Example: build_xml_element
# ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns  the string =
# "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

# keyworded arguments :)
def build_xml_element(tag: str, content: str, **kwargs) -> str:
    # f-Strings. like str.format(), but better. Similar with "${var}" in JS
    rv = f"<{tag}"
    for k, v in kwargs.items():
        rv += f" {k}=\"{v}\""
    rv += f">{content}</{tag}>"
    return rv


# print(build_xml_element("a", "Hello there",
#       href="http://python.org", _class="my-link", id="someid"))


# 5. 5. The validate_dict function that receives as a parameter a set of tuples
# ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
# A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix".
# The function will return True if the given dictionary matches all the rules, False otherwise.

# Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} =>
# False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.

def validate_tuple(key, key_prefix, key_middle, key_suffix):
    if not (key.startswith(key_prefix) and key.endswith(key_suffix)):
        return False

    return key_middle in key[1:-1]


def validate_dict(s: set[tuple[str, str, str, str]], d: dict[str]) -> bool:
    for k, prefix, middle, suffix in s:
        if k not in d:
            return False

        if not validate_tuple(d[k], prefix, middle, suffix):
            return False

    return True


# print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {
#       "key1": "come inside, it's too cold out", "key2": "this is not valid"}))

# 6. 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list, and b representing the number of duplicate elements
# in the list (use sets to achieve this objective).


def count_elements(l: list) -> tuple[int, int]:
    let_set_l = len(set(l))
    return let_set_l, len(l) - let_set_l

# 7. Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two:
# reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.

# Ex: {1,2}, {2, 3} =>
# {
#     "{1, 2} | {2, 3}":  {1, 2, 3},
#     "{1, 2} & {2, 3}":  { 2 },
#     "{1, 2} - {2, 3}":  { 1 },
#     ...
# }


def print_set(s: set) -> str:
    if len(s) == 0:
        return "{}"
    return str(s)


def get_operations_for_2(set1: set, set2: set) -> str:
    return f"{print_set(set1)} | {print_set(set2)}: {print_set(set1 | set2)}\n" \
           f"{print_set(set1)} & {print_set(set2)}: {print_set(set1 & set2)}\n" \
           f"{print_set(set1)} - {print_set(set2)}: {print_set(set1 - set2)}\n" \
           f"{print_set(set2)} - {print_set(set1)}: {print_set(set2 - set1)}\n"


def get_all_operations(*set_args) -> str:
    rv = ""
    for i in range(len(set_args)):
        for j in range(i + 1, len(set_args)):
            rv += get_operations_for_2(set_args[i], set_args[j]) + "\n"

    return rv


# print(get_all_operations({1, 2}, {2, 3}, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))


# 8. Write a function that receives a single dict parameter named mapping.
# This dictionary always contains a string key "start".
# Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way:
# the value of the current key is the key for the next value, until you find a loop (a key that was visited before).
# The function must return the list of objects obtained as previously described.

# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']

class MappingIterator:
    def __init__(self, mapping: dict):
        self.mapping = mapping
        self.current_key = "start"
        self.visited_keys = {"start"}

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_key not in self.mapping:
            raise StopIteration

        self.current_key = self.mapping[self.current_key]
        if self.current_key in self.visited_keys:
            raise StopIteration

        self.visited_keys.add(self.current_key)
        return self.current_key


def follow_mapping(mapping: dict) -> list:
    return list(MappingIterator(mapping))


# print(follow_mapping({'start': 'a', 'b': 'a', 'a': '6',
#       '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# 9. Write a function that receives a variable number of positional arguments and a variable number of keyword arguments adn will
# return the number of positional arguments whose values can be found among keyword arguments values.

# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3

def my_function(*positional_args, **keyword_args) -> int:
    # to be faster? I guess
    keyword_values = set(keyword_args.values())
    positional_args_set = set(positional_args)

    return len(keyword_values & positional_args_set)


# print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
