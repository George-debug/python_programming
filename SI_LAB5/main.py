from Crypto.Util.number import getPrime, isPrime
import random
import OpenSSL
import datetime
from hashlib import sha256


def generate_p_q():
    p = 0
    q = 0
    while not isPrime(p):
        q = p = getPrime(512)
        p = 2 * q + 1
    return p, q


def create_x_y(m: int):

    i = 512

    while m >> i == 0:
        i -= 1

    x = m >> i
    y = m & (2 ** i - 1)

    return x, y


def generate_alpha_beta(p):
    alpha = getPrime(512)

    c = random.randint(2, p - 2)
    beta = pow(alpha, c, p)

    return alpha, beta


def h(x, y, alpha, beta, p):
    return (pow(alpha, x, p) * pow(beta, y, p)) % p


def calc_sha256(m: int):
    m = m.to_bytes(1024, byteorder='big')
    m = str(m)
    m = m.encode('utf-8')
    key = OpenSSL.crypto.PKey()

    return OpenSSL.crypto.sign(key, m, 'sha256')


def calc_sha256_2(m: int):
    m = m.to_bytes(1024, byteorder='big')
    m = str(m)
    m = m.encode('utf-8')

    return sha256(m).hexdigest()


def time_h(m: int):
    start = datetime.datetime.now()
    p, q = generate_p_q()
    x, y = create_x_y(m)
    alpha, beta = generate_alpha_beta(p)

    result = h(x, y, alpha, beta, p)
    end = datetime.datetime.now()
    result = hex(result)

    return end - start, result


def time_sha256(m: int):
    start = datetime.datetime.now()
    result = calc_sha256_2(m)
    end = datetime.datetime.now()

    return end - start, result


def main():
    tests = 30
    total_time_h = datetime.timedelta()
    total_time_sha256 = datetime.timedelta()

    file = open('results.txt', 'w')

    for _ in range(tests):
        m = random.randint(0, 2 ** 1024)
        time_h_, result_h = time_h(m)
        time_sha256_, result_sha256 = time_sha256(m)

        print(f"m: {m}")
        print(f"result_h: {result_h}")
        print(f"result_sha256: {result_sha256}")
        print("\n")

        file.write(f"m: {m}\n")
        file.write(f"result_h: {result_h}\n")
        file.write(f"result_sha256: {result_sha256}\n")
        file.write("\n")

        total_time_h += time_h_
        total_time_sha256 += time_sha256_

    print(f'Average time for h: {total_time_h / tests}')
    print(f'Average time for sha256: {total_time_sha256 / tests}')

    file.write(f'Average time for h: {total_time_h / tests}\n')
    file.write(f'Average time for sha256: {total_time_sha256 / tests}\n')

    file.close()


main()
