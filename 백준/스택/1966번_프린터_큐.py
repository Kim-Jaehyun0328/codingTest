import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n, find = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))
    idx = 0
    ans = 1
    while True:
        if num[idx] == max(num[idx:]):
            if idx % n == find:
                print(ans)
                break
            idx += 1
            ans += 1
            num.append(0)
        else:
            num.append(num[idx])
            idx += 1

