def count_bits(n):
    count = 0

    while n:
        if n & 1:
            count += 1
        
        n >>= 1


    return count


print(count_bits(int(input())))