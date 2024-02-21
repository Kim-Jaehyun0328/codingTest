# def binary_search(arr, target, start, end):
#     while start <= end:
#         mid = (start+end)//2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] > target:
#             end = mid - 1
#         elif arr[mid] < target:
#             start = mid + 1
#     return False
#
#
# N, M = 5, 3
# arr1 = [8, 3, 7, 9, 2]
# arr2 = [5, 7, 9]
#
# arr1.sort()
#
# for x in arr2:
#     temp = binary_search(arr1, x, 0, len(arr1) - 1)
#     if temp == False:
#         print("no", end=" ")
#     else:
#         print("yes", end=" ")

N, M = 5, 3
arr1 = [8, 3, 7, 9, 2]
arr2 = [5, 7, 9]
flag = False

arr1.sort()
arr2.sort()

def binary_search(arr, target, start, end):
    global flag

    if start > end:
        flag = True
        return

    mid = (start+end)//2

    if target == arr[mid]:
        return
    elif target > arr[mid]:
        binary_search(arr, target, mid+1, end)
    elif target < arr[mid]:
        binary_search(arr, target, start, mid-1)

    return


for a in arr2:
    flag = False
    binary_search(arr1, a, 0, len(arr1)-1)
    if flag == True:
        print("no")
    else:
        print("yes")






















