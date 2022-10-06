def get_spiral(l):
    if not l:
        return

    rv = ""

    left, top = 0, 0
    right, bottom = len(l[0]), len(l)

    i, j = 0, 0


    # Wanted to make something like Lee's algorithm :( but I think i tested enough
    while left != right and top != bottom:
        for j in range(left, right):
            rv += l[i][j]
        top += 1

        for i in range(top, bottom):
            rv += l[i][j]
        right -= 1

        for j in range(right-1, left-1, -1):
            rv += l[i][j]
        bottom -= 1

        for i in range(bottom-1, top-1, -1):
            rv += l[i][j]
        left += 1

    return rv
    


def main():
    s = input()
    l = []

    while s != "":
        l.append(s)
        if len(s) != len(l[0]):
            print("Not a good word, I'll not gonna add it")
            l.pop(-1)
            
        s = input()

    print(get_spiral(l))

main()