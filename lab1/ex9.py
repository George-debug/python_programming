def most_common(s):
    v = {}

    for c in s:
        if not c.isalpha():
            continue


        if c not in v:
            v[c] = 0
        else:
            v[c] += 1

    max_val = -1
    max_letter = "no letter found"
    for key in v:
        if max_val < v[key]:
            max_val = v[key]
            max_letter = key

    return max_letter



print(most_common(input()))