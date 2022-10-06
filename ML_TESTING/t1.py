def checkLat(a, b, c):
    return a**2 == b**2 + c**2

def f(a, b, c):
    return checkLat(a, b, c) or checkLat(b, a, c) or checkLat(c, a, b)
