N = 10

a = [[0 for _ in range(N)] for _ in range(N)]

i, j = 0, 0
num = 1
while True:
    if num == N*N:
        a[i][j] = num
        break
    if (i ==0 and j < (len(a)-1)) or (a[i-1][j] != 0 and j < len(a)-1 and a[i][j+1] == 0): #오른쪽으로 이동 조건 맨 위, 방향 전환
        a[i][j] = num
        j += 1
    elif (j == (len(a) -1) and i < (len(a) -1)) or (i < len(a) -1 and j < len(a)-1 and a[i][j+1] != 0 and a[i+1][j] == 0): #아래로 이동 조건
        a[i][j] = num
        i += 1
    elif (i == (len(a) -1) and j > 0) or (i < len(a) - 1 and a[i+1][j] != 0 and a[i][j-1] ==0): #좌로 이동
        a[i][j] = num
        j -= 1
    elif (j == 0 and i > 0) or (a[i][j-1] != 0 and a[i-1][j] == 0): #위로 이동 조건
        a[i][j] = num
        i -= 1
    num += 1

for i in range(N):
    for j in range(N):
        print(a[i][j],end=" ")
    print()
