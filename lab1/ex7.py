def extract_number(s):
    n = 0
    i = 0

    while i < len(s):
        if s[i].isdigit():
            while i < len(s) and s[i].isdigit():
                n = n * 10 + int(s[i])
                i += 1

            return n

        i += 1
            


    return "No number found"


def main():
    s = input()

    print(extract_number(s))

main()