# n = 5
# arr = [3, 2, 1, 1, 9]
# arr.sort(reverse=True)
#
#
# for i in range(1, sum(arr)):
#     sum = 0
#     for x in arr:
#         if sum+x <= i:
#             sum += x
#     if sum != i:
#         print(i)
#         break



N = 5
arr = [3,2,1,1,9]
arr.sort()

target = 1

for i in arr:
    if target < i:
        break
    target += i

print(target)


















