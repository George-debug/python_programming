from VoronoyBoundaries import get_triangles
from read_data import csv_to_table, table_to_float, table_to_points


def print_table(table):
    for row in table:
        print(row)


def equals(f1: float, f2: float) -> bool:
    return abs(f1 - f2) < 0.0001


def print_triangles(file):
    table = csv_to_table(file)[1:]
    table = table_to_float(table)
    table_of_points = table_to_points(table)

    print("Points:")
    print_table(table_of_points)
    print("\n\nTriangles:")

    for (i, j, k) in get_triangles(table_of_points):
        if equals(table[i][2], table[j][2]) and equals(table[j][2], table[k][2]):
            continue
        print(
            f"{table_of_points[i]}, {table_of_points[j]}, {table_of_points[k]}")

    print("\n\n")


print_triangles("ex19_data_2.csv")
