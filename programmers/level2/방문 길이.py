def solution(dirs):
    direction = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
    ch = set()
    now = (0, 0)

    for x in dirs:
        nx = now[0] + direction[x][0]
        ny = now[1] + direction[x][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:  # 경계 안이면
            ch.add((now[0], now[1], nx, ny))
            ch.add((nx, ny, now[0], now[1]))
            now = (nx, ny)

    return len(ch) // 2

print(solution("ULURRDLLU"))