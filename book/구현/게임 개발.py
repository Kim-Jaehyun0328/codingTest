def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3


N, M = 4, 4
pos = [1,1]
dir = 0
matrix = [[1, 1, 1, 1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
ch = [[0 for _ in range(M)] for _ in range(N)]
ch[pos[0]][pos[1]] = 1
answer = 1

direction = [0, 1, 2, 3] #북, 동, 남, 서 (시계방향)


dx = [-1, 0, 1, 0]  #북, 동, 남, 서[-1, 0, 1, 0]
dy = [0, 1, 0, -1]


cnt = 0
while True:
    turn_left()
    row = dx[dir] + pos[0]
    column = dy[dir] + pos[1]
    if 0<= row < N and 0<= column < M and matrix[row][column] == 0 and ch[row][column] == 0: #갈 곳이 있다.
        pos = [row, column]
        answer += 1
        ch[row][column] = 1
        cnt = 0
    else:
        cnt += 1

    if cnt == 4:  #4군데 모두 없다.
        pos = [pos[0]+(dx[dir]*-1),pos[1]+(dy[dir]*-1)]
        cnt = 0
        if matrix[pos[0]][pos[1]] == 1:
            break

print(answer)


