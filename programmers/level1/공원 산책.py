def solution(park, routes):
    h = len(park)
    w = len(park[0])
    for i in range(h):
        if "S" in park[i]:
            x = i
            y = park[i].index("S")

    for route in routes:
        op, n = route.split(" ")
        n = int(n)
        if op == "E":  # 동쪽으로 가는 것
            if y + n >= w or "X" in park[x][y:y + n + 1]:
                continue
            else:
                y = y + n
        elif op == "W":  # 서쪽으로 가는 것
            if y - n < 0 or "X" in park[x][y - n:y + 1]:
                continue
            else:
                y = y - n
        elif op == "S":  # 남쪽으로 가는 것
            if x + n >= h:
                continue
            for i in range(x, x + n + 1):
                if park[i][y] == "X":
                    break
            else:
                x = x + n
        elif op == "N":
            if x - n < 0:
                continue
            for i in range(x - n, x + 1):
                if park[i][y] == "X":
                    break
            else:
                x = x - n
    return [x, y]

print(solution(["OOX", "OXO", "OOS"], ["E 2", "E 3", "N 1"]))