def to_tuple(s):
    return list(map(int, s.split(".")))

def solution(l):
    l.sort(key = to_tuple)
    return l

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))