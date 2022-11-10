from math import sqrt
import numpy as np


def circle_circumscribed(p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]) -> tuple[tuple[float, float], float]:
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    A = np.array([[x3-x1, y3-y1], [x3-x2, y3-y2]])
    Y = np.array([(x3**2 + y3**2 - x1**2 - y1**2),
                 (x3**2+y3**2 - x2**2-y2**2)])
    if np.linalg.det(A) == 0:
        return False
    Ainv = np.linalg.inv(A)
    X = 0.5*np.dot(Ainv, Y)
    x, y = X[0], X[1]
    r = sqrt((x-x1)**2+(y-y1)**2)
    return (x, y), r


def points_in_circle(circle: tuple[tuple[float, float], float], data: list[list[float]]) -> bool:
    (x, y), r = circle
    r = r**2

    for point in data:
        distance = (x - point[0])**2 + (y - point[1])**2
        if distance < r and abs(distance - r) > 0.0001:
            return True

    return False


def get_triangles(data: list[list[float]]):
    triangles = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                circle = circle_circumscribed(data[i], data[j], data[k])
                if circle and not points_in_circle(circle, data):
                    triangles.append((i, j, k))

    return triangles
