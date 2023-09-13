import sys
sys.stdin=open("in1.txt", "r")

n = int(input())
stone = []
dy = [0 for _ in range(n+1)]
for i in range(n):
    a, b, c = map(int, input().split())
    stone.append((a, b, c))
stone.sort(reverse=True)
stone.insert(0, 0)
dy[1] = stone[1][1]
res = 0
for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if stone[j][2] > stone[i][2] and max < dy[j]:
            max = dy[j]
        dy[i] = max + stone[i][1]
    if res < dy[i]:
        res = dy[i]

print(res)

