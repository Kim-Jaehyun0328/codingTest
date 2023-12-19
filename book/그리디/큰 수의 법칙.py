n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]
ans = 0
# data.sort(reverse= True)
#
# ch = 0
# for i in range(m):
#     if ch < k:
#         ans += data[0]
#         ch += 1
#     else:
#         ch = 0
#         ans += data[1]
#
# print(ans)

data.sort()
first = data[-1]
second = data[-2]

cnt = m//(k+1)
rest = m%(k+1)

ans += ((first*k) + (second)) * cnt

ans += first * rest

print(ans)






















