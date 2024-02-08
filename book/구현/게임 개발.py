# def turn_left():
#     global dir
#     dir -= 1
#     if dir == -1:
#         dir = 3
#
#
# N, M = 4, 4
# pos = [1,1]
# dir = 0
# matrix = [[1, 1, 1, 1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
# ch = [[0 for _ in range(M)] for _ in range(N)]
# ch[pos[0]][pos[1]] = 1
# answer = 1
#
# direction = [0, 1, 2, 3] #북, 동, 남, 서 (시계방향)
#
#
# dx = [-1, 0, 1, 0]  #북, 동, 남, 서[-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# cnt = 0
# while True:
#     turn_left()
#     row = dx[dir] + pos[0]
#     column = dy[dir] + pos[1]
#     if 0<= row < N and 0<= column < M and matrix[row][column] == 0 and ch[row][column] == 0: #갈 곳이 있다.
#         pos = [row, column]
#         answer += 1
#         ch[row][column] = 1
#         cnt = 0
#     else:
#         cnt += 1
#
#     if cnt == 4:  #4군데 모두 없다.
#         pos = [pos[0]+(dx[dir]*-1),pos[1]+(dy[dir]*-1)]
#         cnt = 0
#         if matrix[pos[0]][pos[1]] == 1:
#             break
#
# print(answer)
#
#


# 0: 북, 1: 동, 2: 남, 3:서
# 방문을 했으면 매트릭스에서 2로 체크하기

# ans = 1
#
# N, M = 4, 4
#
# A, B, dir = 1, 1, 0
#
# nx = [-1,0,1,0]
# ny = [0,-1,0,1]  # 북서남동 순으로 이동
#
# matrix = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
# matrix[A][B] = 2
#
# def turn_left(dir):
#     if dir + 1 > 3: #북쪽에서 왼쪽 방향으로 회전할때는 서쪽이 된다.
#         return 0
#     else:
#         return dir + 1
#
#
# while True:
#     cnt = 0 #상하좌우 다 돌았는지 체크
#     for _ in range(4):
#         dir = turn_left(dir)
#         dx = nx[dir] + A
#         dy = ny[dir] + B
#         if 0 <= dx < N and 0 <= dy < M and matrix[dx][dy] == 0:  # 갈 수 있는 곳이라면
#             A, B = dx, dy
#             matrix[dx][dy] = 2  # 간 곳으로 체크
#             ans += 1
#             break
#         else:
#             cnt += 1
#     if cnt == 4: #상하좌우 모두 갈 곳이 없다면 뒤로 가야 함
#         dx = nx[(dir+2)%4] + A
#         dy = ny[(dir+2)%4] + B
#         if 0<=dx<N and 0<=dy<M and matrix[dx][dy] != 1: # 갈 수 있다면
#             A, B = dx, dy
#         else:
#             break
#
#
#
# print(ans)



def turn_left(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction

answer = 1
x, y, direction = 1, 1, 0
arr = [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]]
length = len(arr)
arr[x][y] = 2 #현재 위치는 방문한 곳으로 체크하기
steps = [(-1,0), (0,1), (1,0), (0,-1)]

cnt = 0
while True:
    direction = turn_left(direction)

    nx = x + steps[direction][0]
    ny = y + steps[direction][1]
    if 0<=nx<length and 0<=ny<length and arr[nx][ny] == 0:
        arr[nx][ny] = 2 #간 곳으로 체크
        x, y = nx, ny
        answer += 1
        cnt = 0
        continue
    else:
        cnt +=1

    if cnt == 4: #4방향 모두 갈 곳이 없다면
        nx = x - steps[direction][0] #바라보는 방향 반대로 가야하기 때문에 "빼기"를 한다.
        ny = y - steps[direction][1]
        if 0<=nx<length and 0<=ny<length and arr[nx][ny] == 0:
            x = nx
            y = ny
            cnt = 0
        else:
            break




print(answer)




