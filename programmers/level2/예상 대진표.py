import math
n, a, b = 16, 4, 7

answer = 1

while n != 1:
    if (a >= n//2 and b >= n//2) or (a <= n//2 and b <= n//2):
        answer += 1
        n//=2
    else:
        print(int(math.log2(n)))
        break

print(answer)
