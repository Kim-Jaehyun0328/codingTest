ans = 0
n = 5
arr = [2, 3, 1, 2, 2]

arr.sort(reverse=True)


cnt = 0
for i in range(len(arr)):
    if cnt == 0:
        ans += 1
        cnt = arr[i]
    cnt -= 1

print(ans)