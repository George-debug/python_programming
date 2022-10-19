import random 


 

def next_neighbour(line: list[int]) -> int:
    line_sum = sum(line)
    if line_sum == 0:
        return None

    next_neighbour = random.randint(0, line_sum - 1)

    for i, value in enumerate(line):
        if next_neighbour < value:
            return i
        next_neighbour -= value

    return None

def run_once(adjacency_matrix: list[list[int]]) -> int:
    current_line = 0

    while True:
        next_line = next_neighbour(adjacency_matrix[current_line])
        if next_line is None:
            return current_line
        current_line = next_line


def run_for_n_times(adjacency_matrix: list[list[int]], n: int) -> list[float]:
    # create a list of n elements with value 0
    result = {}

    for _ in range(n):
        result_of_run = run_once(adjacency_matrix)
        result[result_of_run] = result.get(result_of_run, 0) + 1

    for key in result:
        result[key] /= n

    return result

# 1 loop 2 ends
matrix = [
    [0, 1, 1, 0], # 0 -> 1, 2
    [1, 0, 0, 1], # 1 -> 0, 3
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

# exercise 1
matrix2 = [
    [0, 1, 0, 0, 0, 1], # 0 -> 1, 5
    [4, 0, 0, 3, 2, 0], # 1 -> 0, 3, 4
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

# 3 loops 3 ends
matrix3 = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


matrix3_2 = [
    [0, 2, 1, 0, 0], # 0 -> 1, 2
    [0, 0, 0, 3, 4], # 1 -> 3, 4
    [0, 0, 0, 0, 0], # 2 -> 2
    [0, 0, 0, 0, 0], # 3 -> 3
    [0, 0, 0, 0, 0], # 4 -> 4
]

matrix3_3 = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


print (run_for_n_times(matrix3, 1000000))
print("\nrun2: ")
print (run_for_n_times(matrix3_2, 1000000))


print (run_for_n_times(matrix3_3, 1000000))