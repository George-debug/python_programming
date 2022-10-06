def count(s):
    vowels = 0
    for c in s:
        if c.lower() in "aeiou":
            vowels += 1

    return vowels

def count2(s):
    # yep, generator :) not list
    p = (1 for c in s if c.lower() in 'aeiou')

    return sum(p)

def main():
    s = input()

    print(count2(s))


main()