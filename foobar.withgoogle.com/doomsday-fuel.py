from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

class Ratio:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return  "(" + str(self.num) + "/" + str(self.den) + ")"

    def is_one(self):
        return self.num == self.den

    def __add__(self, other):
        if isinstance(other, Ratio):
            return Ratio(self.num * other.den + other.num * self.den, self.den * other.den)
        elif isinstance(other, int):
            return Ratio(self.num + other * self.den, self.den)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Ratio):
            return Ratio(self.num * other.num, self.den * other.den)
        elif isinstance(other, int):
            return Ratio(self.num * other, self.den)

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self + (-other)

    def __neg__(self):
        return Ratio(-self.num, self.den)

    def __truediv__(self, other):
        return self * other.inverse()

    def __div__(self, other):
        return self.__truediv__(other)

    def inverse(self):
        return Ratio(self.den, self.num)


def symplify_ratio(ratio: Ratio):
    greates_common_divisor = gcd(ratio.num, ratio.den)
    ratio.num //= greates_common_divisor
    ratio.den //= greates_common_divisor

def transpose_matrix(m):
    return list(map(list,zip(*m)))

def get_matrix_minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def get_matrix_deternminant(m: list[list[Ratio]]) -> Ratio:
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*get_matrix_deternminant(get_matrix_minor(m,0,c))
    return determinant

def get_matrix_inverse(m):
    determinant = get_matrix_deternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = get_matrix_minor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * get_matrix_deternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose_matrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def multiply_2_matrices(A: list[list[Ratio]], B: list[list[Ratio]]):
    rv = []
    for i in range(0,len(A)):
        line=[]
        for j in range(0,len(B[0])):
            s = 0
            for k in range(0,len(A[0])):
                s += A[i][k]*B[k][j]
            line.append(s)
        rv.append(line)

    return rv


def adjacency_matrix_to_ratio(adjacency_matrix):
    rv = []
    for i in range(len(adjacency_matrix)):
        sum_of_line = sum(adjacency_matrix[i])
        if sum_of_line == 0:
            line = [Ratio(0, 1) for _ in range(len(adjacency_matrix))]
            line[i] = Ratio(1, 1)
            rv.append(line)
        else:
            rv.append([Ratio(value, sum_of_line) if value != 0 else Ratio(0, 1) for value in adjacency_matrix[i]])

    return rv

def get_R_and_Q(graph: list[list[Ratio]]) -> (list[list[Ratio]], list[list[Ratio]]):
    R = []
    Q = []
    for i in range(len(graph)):
        if graph[i][i].is_one():
            continue

        R_line = []
        Q_line = []

        for j in range(len(graph[i])):
            if graph[j][j].is_one():
                R_line.append(graph[i][j])
            else:
                Q_line.append(graph[i][j])

        R.append(R_line)
        Q.append(Q_line)

    return R, Q

def I_munus_Q(Q: list[list[Ratio]]):
    for i in range(len(Q)):
        for j in range(len(Q[i])):
            Q[i][j].num *= -1
            if i == j:
                Q[i][j].num += Q[i][j].den

# def print_table(graph: list[list[Ratio]]):
#     for i in range(len(graph)):
#         to_print = "[ "
#         for j in range(len(graph[i])):
#             if graph[i][j].num != 0:
#                 symplify_ratio(graph[i][j])
#             to_print += str(graph[i][j]) + " "
#         to_print += "]"

#         print(to_print)

def ratio_line_to_int(ratio_line):
    common_denominator = 1
    for ratio in ratio_line:
        symplify_ratio(ratio)
        common_denominator = lcm(common_denominator, ratio.den)
    for i in range(len(ratio_line)):
        ratio_line[i].num *= (common_denominator // ratio_line[i].den)
        ratio_line[i].den = common_denominator
    return [ratio.num for ratio in ratio_line] , common_denominator

def simplify_fractions(numerators, denominator):
    greates_common_divisor = denominator
    for num in numerators:
        greates_common_divisor = gcd(num, greates_common_divisor)
        if (greates_common_divisor == 1):
            return (numerators, denominator)
    return ([num // greates_common_divisor for num in numerators], denominator // greates_common_divisor)

def solution(m):
    if len(m) == 1:
        return [1, 1]

    graph = adjacency_matrix_to_ratio(m)
    R, Q = get_R_and_Q(graph)
    I_munus_Q(Q)
    # print("\n==========  Q  ==========\n")
    # print_table(Q)

    Q_inverse = get_matrix_inverse(Q)
    # print("\n========== (I - Q)^2 ==========\n")
    # print_table(Q_inverse)

    RQ_inverse = multiply_2_matrices(Q_inverse, R)
    # print("\n========== (I - Q)^2 * R ==========\n")
    # print_table(RQ_inverse)

    numerators, denominator = ratio_line_to_int(RQ_inverse[0])
    numerators, denominator = simplify_fractions(numerators, denominator)

    # print("\n========== Numerators ==========\n")
    # print(numerators)

    return numerators + [denominator]


test = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]

print(solution(test))

