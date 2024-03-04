# n, m = 2, 100
#
# dy = [0 for _ in range(1001)]
#
# dy[1] = 1
# dy[2] = 3
#
# for i in range(3, 1001):
#     dy[i] = (dy[i-1] + 2*dy[i-2])%796796
#
# print(dy[m])

n = 3
dy = [0 for _ in range(1001)]

dy[1] = 1
dy[2] = 3

for i in range(3, n+1):
    dy[i] = (dy[i-1] + dy[i-2] * 2) % 769769

print(dy[n])



















