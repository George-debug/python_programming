# 1. Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters.

import os
import re


def extract_words(text):
    return re.findall(r'[a-zA-Z1-9]+', text)


print(extract_words('Hello, world!'))


# 2. Write a function that receives as a parameter a regex string, a text string and a whole number x,
# and returns those long-length x substrings that match the regular expression.

def extract_words_with_regex(regex, text, x):
    return list(filter(lambda s: len(s) == x, re.findall(regex, text)))


print(extract_words_with_regex(
    r'[a-zA-Z1-9]+', 'Hello all of you this works!', 5))


# 3. Write a function that receives as a parameter a string of text characters and a list of regular expressions and
# returns a list of strings that match on at least one regular expression given as a parameter.

def extract_words_with_regex_list(text, regex_list):
    word_list = set()

    for regex in regex_list:
        word_list.update(re.findall(regex, text))

    return list(word_list)


print(extract_words_with_regex_list(
    "Hello all of you this works!", [r'\w[a-z]+\w', r'[!]+']))


# 4. Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns
# those elements that have as attributes all the keys in the dictionary and values ​​the corresponding values.
# For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags
# whose attributes are class="url" si name="url-form" si data-id="item".

# this gets tags, but not the once that start with / or ? (like <?xml version="1.0" encoding="UTF-8"?> or closing tags)
tags_regex = r'<(?![/?]).+?>'
keys_values_regex = r'([\w-]+)="(.+?)"'


def get_tags_with_attributes_all(path, attributes):
    with open(path, 'r') as f:
        text = f.read()

    tags = re.findall(tags_regex, text)
    tags_with_attributes = []

    for tag in tags:
        tag_attributes = re.findall(keys_values_regex, tag)

        # print("tag_attributes", tag_attributes)
        # print("tag_attributes", attributes.items())

        if all(attr in tag_attributes for attr in attributes.items()):
            tags_with_attributes.append(tag)

    return tags_with_attributes


print(get_tags_with_attributes_all('sample.xml', {"TestType": "CMD"}))

# 5. Write another variant of the function from the previous exercise that returns those elements that have at
# least one attribute that corresponds to a key-value pair in the dictionary.


def get_tags_with_attributes_any(path, attributes):
    with open(path, 'r') as f:
        text = f.read()

    tags = re.findall(tags_regex, text)
    tags_with_attributes = []

    for tag in tags:
        tag_attributes = re.findall(keys_values_regex, tag)

        if any(attr in tag_attributes for attr in attributes.items()):
            tags_with_attributes.append(tag)

    return tags_with_attributes


print(get_tags_with_attributes_any('sample.xml',
      {"TestType": "CMD", "TestId": "0004"}))


# 6. Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
# Censorship means replacing characters from odd positions with *.

vocal_regex = r'\b([aeiou][a-z]*[aeiou]|[aeiou])\b'


def censor(word):
    return ''.join(['*' if i % 2 == 1 else c for i, c in enumerate(word)])


def censor_words(text):
    return re.sub(vocal_regex, lambda m: censor(m.group(0)), text, flags=re.IGNORECASE)


print(censor_words('I ate the apple and the orange'))

# 7. Verify using a regular expression whether a string is a valid CNP.

# !!!!!!!!!! this is perhaps my favorite exercise from all labs


# https://ro.wikipedia.org/wiki/Cod_numeric_personal_(Rom%C3%A2nia)

cnp_regex = r'^[1-8]\d{2}(?:0[1-9]|1[0-2])(?:[0][1-9]|[12][0-9]|3[01])(?:[0][1-9]|[123][0-9]|4[0-8]|5[12])\d{4}$'


def verify_cnp(cnp):
    return re.match(cnp_regex, cnp) is not None

# Generat cu https://isj.educv.ro/cnp/


print(verify_cnp('6221110017502'))


# 8. Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression
# given as a parameter or contains a string that matches the same expression. Files that satisfy both conditions will be prefixed with ">>"

def search_files_by_name_and_content(path, regex):
    for (root, directories, files) in os.walk(path):
        for file in files:
            match_name = re.match(regex, file) is not None
            try:
                match_content = re.search(regex, open(
                    os.path.join(root, file), 'r', encoding="utf-8").read()) is not None
            except:
                match_content = False

            if match_name and match_content:
                print(">>", file)

            elif match_name or match_content:
                print(file)


search_files_by_name_and_content(
    'C:\\Users\\George\\Desktop\\Cocktail Vault', r'lime|Lime')

search_files_by_name_and_content('.', r'.*\.py')

# this is a .py file
