def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return False


N, M = 5, 3
arr1 = [8, 3, 7, 9, 2]
arr2 = [5, 7, 9]

arr1.sort()

for x in arr2:
    temp = binary_search(arr1, x, 0, len(arr1) - 1)
    if temp == False:
        print("no", end=" ")
    else:
        print("yes", end=" ")