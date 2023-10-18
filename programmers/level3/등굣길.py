def solution(m, n, puddles):
    arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    div = 1000000007
    for x in puddles:
        arr[x[1]][x[0]] = -1

    arr[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i][j] == -1:
                continue
            elif i == 1 and j == 1:
                continue
            if arr[i - 1][j] != -1:
                arr[i][j] += arr[i - 1][j]
            if arr[i][j - 1] != -1:
                arr[i][j] += arr[i][j - 1]

    return arr[n][m] % div


print(solution(4, 3, [[2,2]]))