import csv


def csv_to_table(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        return list(reader)


def table_to_float(table: list[list]) -> list[list]:
    rv = []
    for i in range(len(table)):
        line = []
        for j in range(len(table[i])):
            line.append(float(table[i][j]))
        rv.append(line)

    return rv


def table_to_points(table: list[list]) -> list[list]:
    rv = []
    for i in range(len(table)):
        rv.append((table[i][0], table[i][1]))

    return rv
