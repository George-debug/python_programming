import numpy
import random
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    s = input()
    return (list(s[:len(s) - 1]))


def invr():
    return (map(int, input().split()))


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


def verify_solution(statues, max_ball, k, solution):
    verified = statues.copy()
    for i in range(len(verified)):
        for j in range(k):
            zz = (i - j) % len(statues)
            verified[i] = (verified[i] + solution[zz]) % max_ball

    return verified


def scale_add_rows(matrix, i, j, scale, offset):
    for k in range(offset, len(matrix)):
        matrix[i][k] = matrix[i][k] + matrix[j][k] * scale


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


def get_possible_solutions(a, b, n):
    rv = []
    for i in range(n):
        if (a * i) % n == b:
            rv.append(i)
    return rv


class Problem:
    def __init__(self, statues_size, max_ball, k, statues):
        self.statues_size = statues_size
        self.max_ball = max_ball
        self.k = k
        self.statues = statues

    def __solve(self, matrix, i, j, solution):

        while j < len(matrix[0]) and i < self.statues_size:
            # print("i:", i, "| j:", j)
            if matrix[i][j] == 0:
                return -1

            if matrix[i][j] != 1:
                try:
                    p = pow(matrix[i][j], -1, self.max_ball)

                    for new_j in range(len(matrix[0])):
                        matrix[i][new_j] = (
                            matrix[i][new_j] * p) % self.max_ball
                    solution[i] = (solution[i] * p) % self.max_ball

                except Exception as _:
                    print("cant")
                    print_matrix(matrix, solution)

                    possible_solutions = get_possible_solutions(
                        matrix[i][j], solution[i], self.max_ball)

                    # print("possible solutions:", possible_solutions)

                    if len(possible_solutions) == 0:
                        return -1

                    best_solution = -1
                    for possible_solution in possible_solutions:
                        new_matrix = [x[j+1:] for x in matrix]
                        new_solution = solution.copy()
                        for k in range(len(new_solution)):
                            new_solution[k] = (
                                new_solution[k] - possible_solution * matrix[k][j]) % self.max_ball
                        new_solution[i] = possible_solution
                        # print("trying:", possible_solution)
                        # print_matrix(new_matrix, new_solution)
                        rv = self.__solve(new_matrix, i+1, 0, new_solution)
                        # print("rv:", rv)
                        if rv != -1:
                            if rv == 0:
                                return 0
                            else:
                                if best_solution == -1:
                                    best_solution = rv
                                else:
                                    best_solution = min(best_solution, rv)

                    return best_solution

            # print("before")
            # print("i:", i, "| j:", j)
            # print_matrix(matrix, solution)

            for new_i in range(self.statues_size):
                if i == new_i or matrix[new_i][j] == 0:
                    continue
                p = matrix[new_i][j] * -1
                # print("new_i:", new_i, "| p:", p)
                scale_add_rows(matrix, new_i, i, p, j)
                solution[new_i] = solution[new_i] + solution[i] * p

            # print("after")
            # print_matrix(matrix, solution)

            i += 1
            j += 1

        # print("i to ", self.statues_size, "| j to ", len(matrix[0]))
        # print("verify:", verify_solution(
            # self.statues, self.max_ball, self.k, solution))

        rv = 0
        for i in range(self.statues_size):
            aux = solution[i] % self.max_ball
            if aux != 0:
                to_up = self.max_ball - aux
                if to_up < aux:
                    rv += to_up
                else:
                    rv += aux

        return rv

    def solve(self):
        matrix = getMatrix(self.statues_size, self.k)
        solution = [0] * self.statues_size
        for i in range(self.statues_size):
            if self.statues[i] != 0:
                solution[i] = self.max_ball - self.statues[i]

        return self.__solve(matrix, 0, 0, solution)


# print(solution(5, 9, 3, [8, 1, 4, 5, 0]))
# print(solution(3, 5, 2, [1, 0, 0]))
# matrix = getMatrix(5, 3)
# remove_xi(matrix, 1)
# print(matrix)
# print(modMatInv(matrix, 9))
# print(verify_solution([8, 1, 4, 5, 0], 9, 3, [1, 4, 1, 2, 1]))
# p1 = Problem(3, 5, 2, [1, 0, 0])
p2 = Problem(5, 9, 3, [8, 1, 4, 5, 0])
# p3 = Problem(5, 5, 2, [1, 0, 0, 0, 0])
# p4 = Problem(4, 4, 2, [1, 0, 0, 0])
print(p2.solve())

# n, m, k = inlt()
# statues = inlt()


# print(verify_solution([8, 1, 4, 5, 0], 9, 3, [-3, 3, -4, -4, -1]))


# def modMatInv(A, p):       # Finds the inverse of matrix A mod p
#     n = len(A)
#     A = numpy.matrix(A)
#     adj = numpy.zeros(shape=(n, n))
#     for i in range(0, n):
#         for j in range(0, n):
#             adj[i][j] = (
#                 (-1)**(i+j)*int(round(numpy.linalg.det(minor(A, j, i))))) % p
#     return (modInv(int(round(numpy.linalg.det(A))), p)*adj) % p


# def modInv(a, p):          # Finds the inverse of a mod p, if it exists
#     for i in range(1, p):
#         if (i*a) % p == 1:
#             return i
#     raise ValueError(str(a)+" has no inverse mod "+str(p))


# def minor(A, i, j):    # Return matrix A with the ith row and jth column deleted
#     A = numpy.array(A)
#     minor = numpy.zeros(shape=(len(A)-1, len(A)-1))
#     p = 0
#     for s in range(0, len(minor)):
#         if p == i:
#             p = p+1
#         q = 0
#         for t in range(0, len(minor)):
#             if q == j:
#                 q = q+1
#             minor[s][t] = A[p][q]
#             q = q+1
#         p = p+1
#     return minor


# maatrix = getMatrix(5, 2)
# maatrix = modMatInv(maatrix, 5)

# print(maatrix)
