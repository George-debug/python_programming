import sys

def cmmdc(a, b):
    while b:
        a, b = b, a % b
    return a


# pe asta nu pot sa-l fac dintr-o linie :(
def cmmdc2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

def main():
    # dupa o sa folosesc input :)
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    print(cmmdc(a, b))

main()