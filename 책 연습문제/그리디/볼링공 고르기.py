# n, m = 8, 5
# arr = [1,5,4,3,2,4,5,2]
# ans = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         if arr[i] != arr[j]:
#             ans += 1
#
# print(ans)


N, M = 8, 5
arr = [1,5,4,3,2,4,5,2]

# ans = 0
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] != arr[j]:
#             print(i+1, j+1)
#             ans += 1


weight = [0 for _ in range(11)]
ans= 0
for x in arr:
    weight[x] += 1


for i in range(1, M+1):
    N -= weight[i] #현재 무게 말고 선택할 수 있는 경우의 수
    ans += (N * weight[i])



print(ans)

























