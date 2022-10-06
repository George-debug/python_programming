# ultimul pe care-l scriu in romana :)

def aparitii(s1, s2):

    i = 0
    count = 0
    while len(s2) - i >= len(s1):
        sub_str = s2[i:i+len(s1)]

        if sub_str == s1:
            count += 1

        i += 1

    return count


def main():
    str1 = input()
    str2 = input()

    print(aparitii(str1, str2))

main()