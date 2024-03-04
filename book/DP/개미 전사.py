# n = 4
# arr = [1, 3, 1, 5]
# dy = [0 for _ in range(n)]
# dy[0] = arr[0]
# dy[1] = max(arr[0], arr[1])
#
# for i in range(2, n):
#     dy[i] = max(dy[i - 1], dy[i - 2] + arr[i])
# print(dy[n - 1])

n = 4
arr = [1,3,1,5]
dy = [0 for _ in range(101)]

dy[0] = arr[0]
dy[1] = max(arr[0], arr[1])

for i in range(2, len(arr)):
    dy[i] = max(dy[i-1], dy[i-2] + arr[i])

print(dy[n-1])




















