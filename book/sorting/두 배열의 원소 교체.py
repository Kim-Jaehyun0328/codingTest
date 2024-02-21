N, K = 5, 3
arr1 = [1, 2, 5, 4, 3]
arr2 = [5, 5, 6, 6, 5]

arr1.sort()
arr2.sort()

for i in range(K):
    if arr1[i] < arr2[-(i+1)]:
        arr1[i], arr2[-(i+1)] = arr2[-(i+1)], arr1[i]

print(sum(arr1))