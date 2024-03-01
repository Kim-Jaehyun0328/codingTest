# def binary_search(arr, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         cnt = 0
#         for x in arr:
#             if (x-mid) > 0:
#                 cnt += (x-mid)
#         if cnt == target:
#             return mid
#         elif cnt < target:
#             end = mid - 1
#         elif cnt > target:
#             start = mid + 1
#
#
# N, M = 4, 6
# arr = [19, 15, 10, 17]
#
# print(binary_search(arr, M, 0, max(arr)))

N, M = 4, 6
arr = [19, 15, 10, 17]




def binary_search(arr, target, start, end):
    mid = (start+end)//2
    cnt = 0

    for x in arr:
        if (x - mid) > 0:
            cnt += (x - mid)


    if cnt == target:
        return mid
    elif cnt < target:
        return binary_search(arr, target, start, mid-1)
    elif cnt > target:
        return binary_search(arr, target, mid+1, end)

    return


print(binary_search(arr, M, 0, max(arr)))

















