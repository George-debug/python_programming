def word_count(s):
    return sum(1 for i in s.split(" ") if i != "")

print(word_count(input()))