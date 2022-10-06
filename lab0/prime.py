def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # max = n**0.5 + 1
    # i = 3
    # while i < max:
    #     if n % i == 0:
    #         return False
    #     i += 2
    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0:
            return False

    return True
