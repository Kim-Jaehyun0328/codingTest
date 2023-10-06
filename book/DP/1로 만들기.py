x = 26

dy = [0 for _ in range(30001)]



for i in range(2, x+1):

    dy[i] = dy[i-1]+1

    if i%2 == 0:
        dy[i] = min(dy[i], dy[i//2]+1)
    if i%3 == 0:
        dy[i] = min(dy[i], dy[i//3]+1)
    if i%5 == 0:
        dy[i] = min(dy[i], dy[i//5]+1)

print(dy[x])