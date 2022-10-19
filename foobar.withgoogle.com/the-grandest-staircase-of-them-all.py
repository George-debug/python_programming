def p(bb, HH):
    map_bH = {}
    stack_bH = [(bb, HH)]

    while stack_bH:
        b, H = stack_bH[-1]

        if b not in map_bH:
            map_bH[b] = {}
            continue
        elif H not in map_bH[b]:
            if H == 0 or b == 0:
                map_bH[b][H] = 0
            elif b == 1:
                map_bH[b][H] = 1
            elif H == 1:
                map_bH[b][H] = 0
            else:
                ok = True

                sum = 0
                for i in range(2, min(b-1, H)+1):
                    new_b, new_H = b-i, i-1
                    if new_b not in map_bH or new_H not in map_bH[new_b]:
                        stack_bH.append((new_b, new_H))
                        ok = False
                        continue

                    sum += map_bH[new_b][new_H]
                
                if ok:
                    if b <= H:
                        sum += 1
                    # print(b, H, sum)
                    map_bH[b][H] = sum
                else:
                    continue
            

        stack_bH.pop()

    # print(map_bH)
    return map_bH[bb][HH]

def solution(n):
    return p(n, n-1)

print(solution(200))