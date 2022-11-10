def gray(n) -> str:
    x = n ^ (n >> 1)
    return bin(x)[2:]


n = 73
print(gray(n))
print(gray(-n))
