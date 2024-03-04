# n = 3
# m = 7
# arr = [2, 3, 5]
# dy = [10001 for _ in range(m + 1)]
#
# for x in arr:
#     dy[x] = 1
#
# for i in range(n):
#     for j in range(arr[i], m+1):
#         dy[j] = min(dy[j], dy[j-arr[i]]+1)
#
# if dy[m] == 10001:
#     print(-1)
# else:
#     print(dy[m])
#
# print(dy)


n, m = 2, 15
coins = [2, 3]

dy = [10001 for _ in range(m+1)]
dy[0] = 0
for coin in coins:
    dy[coin] = 1

for i in range(n):
    for j in range(coins[i], m+1):
        dy[j] = min(dy[j], dy[j-coins[i]]+1)


if dy[m] == 10001:
    print(-1)
else:
    print(dy[m])

















