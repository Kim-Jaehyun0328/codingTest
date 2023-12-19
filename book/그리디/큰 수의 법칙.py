n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]
ans = 0
data.sort(reverse= True)

ch = 0
for i in range(m):
    if ch < k:
        ans += data[0]
        ch += 1
    else:
        ch = 0
        ans += data[1]

print(ans)