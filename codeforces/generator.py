import random


def getMatrix(statues_size, k):
    rv = []
    for i in range(statues_size):
        rv.append([0] * statues_size)
        index = i
        for _ in range(k):
            rv[i][index] = 1
            index -= 1
            if index < 0:
                index = statues_size - 1
    return rv


def print_matrix(matrix, statues):
    lines = ["" for _ in range(len(matrix))]
    print("-" * 20)
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            lines[i] += str(matrix[i][j]) + " "

        max_len = max([len(x) for x in lines])
        for i in range(len(lines)):
            lines[i] += " " * (max_len - len(lines[i]))

    for i in range(len(lines)):
        print(lines[i], "|", statues[i])

    print("-" * 20 + "\n\n")


max_ball = 11
statues_size = 11
k = 4


def get_solution(statues):
    solution = [0] * statues_size
    for i in range(statues_size):
        if statues[i] != 0:
            solution[i] = max_ball - statues[i]

    return solution

# i += scale * j


def scale(l, scale):
    return [x * scale for x in l]


def add(l1, l2):
    return [x + y for x, y in zip(l1, l2)]


matrix = getMatrix(statues_size, k)
statues = [random.randint(0, max_ball) for _ in range(statues_size)]
solution = get_solution(statues)

for i in range(len(matrix)):
    # print("i:", i)
    if matrix[i][i] == 0:
        print("end")
    if matrix[i][i] != 1:
        try:
            scale_p = pow(matrix[i][i], -1, max_ball)
            matrix[i] = scale(matrix[i], scale_p)
            matrix[i] = [x % max_ball for x in matrix[i]]
            # print("scale:", scale_p)
        except:
            print("end, bad scale")
            break
    rv = []
    for j in range(len(matrix)):

        if i == j:
            rv.append(0)
            continue
        else:
            rv.append(matrix[j][i])

        if matrix[j][i] == 0:
            continue

        scale_p = -matrix[j][i]

        matrix[j] = add(matrix[j], scale(matrix[i], scale_p))
        matrix[j] = [x % max_ball for x in matrix[j]]

    print(rv)
