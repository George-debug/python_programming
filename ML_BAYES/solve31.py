from Ratio import Ratio
import csv

p_y = [Ratio(1, 2), Ratio(1, 2)]

p_x32 = [
    [
        [
            Ratio(3, 10), Ratio(3, 10)
        ],  # x0
        [
            Ratio(9, 10) ** 2, Ratio(1, 10) ** 2
        ]  # x1
    ],  # y = 0
    [
        [
            Ratio(2, 10), Ratio(8, 10)
        ],  # x0
        [
            Ratio(5, 10) ** 2, Ratio(5, 10) ** 2
        ]  # y = 1
    ]
]

p_x33 = [
    [
        [Ratio(3, 4), Ratio(1, 4)],  # x0
        [Ratio(2, 4), Ratio(2, 4)],  # x1
        [Ratio(1, 4), Ratio(3, 4)]  # x2
    ],  # y = 0
    [
        [Ratio(1, 4), Ratio(3, 4)],  # x0
        [Ratio(2, 4), Ratio(2, 4)],  # x1
        [Ratio(3, 4), Ratio(1, 4)]  # x2
    ],  # y = 1
]


def x33_func(x0: int, x1: int, x2: int) -> int:
    x0 = x0 == 1
    x1 = x1 == 1
    x2 = x2 == 1

    result = (x0 and x1) or not (x1 or x2)

    return 1 if result else 0


def calculate_x33():
    for x0 in range(2):
        for x1 in range(2):
            for x2 in range(2):
                print(f"{x0}  | {x1}  | {x2}  | {x33_func(x0, x1, x2)}")


class MatrixProbabilitiesIterator:
    def __init__(self, matrix: list[list[Ratio]]):
        self._matrix = matrix
        self._values = [0] * len(matrix)
        self._values[0] = -1

    def __iter__(self):
        return self

    def __next__(self):
        i = 0
        carry = 1
        while i < len(self._values) - 1:
            if carry == 1:
                self._values[i] += 1
                carry = 0
            if self._values[i] == len(self._matrix[i]):
                self._values[i] = 0
                carry = 1
            else:
                break
            i += 1

        self._values[-1] += carry

        if self._values[-1] >= len(self._matrix[-1]):
            raise StopIteration

        return self._values
# for every val in y, for every index in x, for every val in x


def get_naive_bayes(prob_y: list[Ratio], prob_x_cond_y: list[list[list[Ratio]]]) -> list[tuple[list[int], Ratio]]:
    result = []
    for y in range(len(prob_y)):
        result.append([])
        for index_list in MatrixProbabilitiesIterator(prob_x_cond_y[y]):
            conditional_prob = Ratio(1, 1)
            for index_of_index in range(len(index_list)):
                conditional_prob *= prob_x_cond_y[y][index_of_index][index_list[index_of_index]]
            prob = conditional_prob * prob_y[y]
            prob.simplify()
            result[y].append((index_list.copy(), prob))

    return result


def print_naive_bayes(naive_bayes: list[tuple[list[int], Ratio]]):
    error_rate = Ratio(0, 1)
    for index_of_index_list in range(len(naive_bayes[0])):
        for y in range(len(naive_bayes)):
            index_list, prob = naive_bayes[y][index_of_index_list]
            to_print = f"Y = {y}, "
            for index_in_index_list in range(len(index_list)):
                to_print += f"x{index_in_index_list} = {index_list[index_in_index_list]}, "

            to_print = to_print[:-2]
            print(f"P{to_print}) = {prob}")

        answer = 1 if naive_bayes[1][index_of_index_list][
            1] > naive_bayes[0][index_of_index_list][1] else 0

        error_rate += naive_bayes[1 - answer][index_of_index_list][1]

        print(
            f"---------------------- decision: {answer} ----------------------\n")

    error_rate.simplify()
    print(f"error rate: {error_rate}")


def csv_to_table(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        return list(reader)


def get_p_y_p_x34():
    # read from data34.csv
    p_x34 = [
        [
            [
                0, 0
            ],  # x0
            [
                0, 0
            ]  # x1
        ],  # y = 0
        [
            [
                0, 0
            ],  # x0
            [
                0, 0
            ]
        ]  # y = 1
    ]

    p_y = [0, 0]
    matrix_34 = csv_to_table("data34.csv")
    matrix_34 = matrix_34[1:]

    for line in matrix_34:
        y = int(line[0])
        x0 = int(line[1])
        x1 = int(line[2])

        p_x34[y][0][x0] += 1
        p_x34[y][1][x1] += 1
        p_y[y] += 1

    sum_y = sum(p_y)

    for i in range(2):
        for j in range(2):
            for k in range(2):
                p_x34[i][j][k] = Ratio(p_x34[i][j][k], p_y[i])
    print(p_x34)

    p_y = [Ratio(p_y[0], sum_y), Ratio(p_y[1], sum_y)]

    for y in range(2):
        for x_index in range(2):
            for x in range(2):
                p_x34[y][x_index][x].simplify()
                print(
                    f"P(x{x_index} = {x} | y = {y}) = {p_x34[y][x_index][x]}")

    return p_y, p_x34


p_y34, p_x34 = get_p_y_p_x34()

results = get_naive_bayes(p_y34, p_x34)

print_naive_bayes(results)
