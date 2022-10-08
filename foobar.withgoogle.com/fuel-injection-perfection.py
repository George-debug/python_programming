

def solution_aux(n):
    if n <= 2:
        return

    map_pallets = {}
    map_pallets[1] = 0
    
    q = [n]

    while q:
        x = q[-1]
        if x & 1:
            next_x = x + 1
            if next_x not in map_pallets:
                q.append(next_x)
                continue
            prev_x = x - 1
            if prev_x not in map_pallets:
                q.append(prev_x)
                continue

            map_pallets[x] = 1 + min(map_pallets[prev_x], map_pallets[next_x])

        else:
            half_x = x//2
            if half_x not in map_pallets:
                q.append(half_x)
                continue

            map_pallets[x] = 1 + map_pallets[half_x]
                
        q.pop()


    return map_pallets[n]


def solution(n):
    n = int(n)

    return solution_aux(n)