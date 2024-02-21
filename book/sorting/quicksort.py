# arr = [5,7,9,0,3,1,6,2,4,8]
#
# def quick_sort(arr, start, end):
#     if start >= end: #데이터가 하나 뿐이라면 종료
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#
#         while left <= end and arr[left] <= arr[pivot]:
#             left += 1
#         while right > start and arr[right] >= arr[pivot]:
#             right -= 1
#
#         if left > right:
#             arr[right], arr[pivot] = arr[pivot], arr[right]
#         else:
#             arr[left], arr[right] = arr[right], arr[left]
#
#         print(arr)
#
#     quick_sort(arr, start, right-1)
#     quick_sort(arr, right+1, end)
#
# quick_sort(arr, 0, len(arr)-1)
# print(arr)


arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left >= right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


quick_sort(arr, 0, len(arr) - 1)
print(arr)
