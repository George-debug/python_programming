import time
import random


def normal(a, b):
    verified = set()
    if a == b:
        return True
    if (a + b) & 1:
        return False
    while a != b:
        if a > b:
            a, b = b, a
        if a in verified:
            return False
        verified.add(a)
        a, b = 2 * a, b - a

    return True


def next_power(x):
    return 1 << (x-1).bit_length()


def mine_aux(a, b):
    sum = a + b
    d, r = divmod(sum, 2 * a)
    if r != 0:
        d += 1

    p = next_power(d)
    next_a = p * a

    return sum - next_a, next_a


maximus = 0


def mine(a, b):
    if a == b:
        return True
    sum = a + b
    if sum & 1:
        return False
    sum_halfed = sum >> 1
    if a > b:
        a, b = b, a

    verified = set()
    i = 0
    while a != b:
        if a in verified:
            return False
        verified.add(a)

        d, r = divmod(sum_halfed, a)
        if r != 0:
            d += 1
        p = next_power(d)
        next_a = p * a
        a, b = sum - next_a, next_a
        i += 1

    return True


if __name__ == '__main__':
    time_normal = 0
    time_mine = 0
    for i in range(10000):
        a = random.randint(1, 20000)
        b = random.randint(1, 20000)

        start = time.time()
        z1 = normal(a, b)
        time_normal += time.time() - start

        start = time.time()
        z2 = mine(a, b)
        time_mine += time.time() - start

        if z1 != z2:
            print(a, b, z1, z2)
            break

    print("normal: ", time_normal)
    print("mine: ", time_mine)
