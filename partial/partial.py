import csv
import os
import sys


def read_csv(file):
    rv = []
    i = 0
    try:
        with open(file, 'r', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                rv.append(row)
                if len(rv[0]) != len(row):
                    raise Exception(f'different words on line{i}')
                i += 1
    except:
        raise Exception('IO error')

    return rv


def problem(file, column):
    if not os.path.exists(file):
        raise Exception('file  not found')

    parsed = read_csv(file)

    counter = 0
    index = -1

    for parsed_index in range(len(parsed[0])):
        column_name = parsed[0][parsed_index]
        if column_name == column:
            counter += 1
            index = parsed_index

    if counter == 0:
        raise Exception('unknown column name')

    if counter > 1:
        raise Exception('invalid format - duplicate columns')

    my_column = set()

    for line_index in range(1, len(parsed)):
        to_add = parsed[line_index][index]
        my_column.add(to_add.lower())

    return my_column


# file = './Problema-1/in.csv'a
try:
    # print(sys.argv)
    file = sys.argv[1]
    column = sys.argv[2]

    parsed_set = problem(file, column)
    print('[OK]')
    for line in parsed_set:
        print(line)
except Exception as e:
    print(f'[ERROR] - {e}')
