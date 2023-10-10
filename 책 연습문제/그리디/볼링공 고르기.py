n, m = 8, 5
arr = [1,5,4,3,2,4,5,2]
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] != arr[j]:
            ans += 1

print(ans)