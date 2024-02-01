def solution(n):
    answer = []
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):

            if i%3 == 0:
                x += 1
            elif i%3 == 1:
                y += 1
            elif i%3 == 2:
                x -= 1
                y -= 1
            arr[x][y] = num
            num += 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])

    return answer

print(solution(4))