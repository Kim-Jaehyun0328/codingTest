import sys

sys.stdin = open("practice", "r")

N = int(input())
K = int(input())


matrix = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1 #사과

L = int(input())
pos = dict()

for _ in range(L):
    a, b = input().split()
    pos[int(a)] = b #L이면 -1, R이면 +1 하면 된다.


#matirx = 판, pos = n초마다 방향 전환 정보


def change_dir(dir, C):

    if C == "L": #왼쪽으로 이동
        dir -= 1
        if dir < 0:
            dir = 3
    else: #오른쪽으로 이동
        dir += 1
        if dir > 3:
            dir = 0
    return dir

answer = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]
dir = 1 #0:북, 1:동, 2:남, 3:서
x, y = 0, 0 #시작 위치
matrix[x][y] = 2 #뱀이 차지하는 공간은 2로 표시
q= [(x, y)]
while True:
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0<=nx<N and 0<=ny<N and matrix[nx][ny] != 2:
        if matrix[nx][ny] == 1: #이동할 곳에 사과가 있다면
            q.append((nx,ny)) #몸통이 커짐
            matrix[nx][ny] = 2
        elif matrix[nx][ny] == 0:
            matrix[nx][ny] = 2
            q.append((nx,ny))
            px, py = q.pop(0)
            matrix[px][py] = 0
        x, y = nx, ny
        answer += 1 #1초가 흐름
        if answer in pos.keys(): #현재 시간이 방향을 바꿔야 하면
            dir = change_dir(dir, pos[answer])
    else:
        answer += 1
        break

print(answer)

