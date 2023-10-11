def binary(arr, start, end):
    global idx
    if start >= end:
        return
    mid = (start+end)//2
    if arr[mid] == mid:
        idx = mid
        return
    else:
        binary(arr, 0, mid-1)
        binary(arr,mid+1, end)

n = 5
arr= [-15,-4,3,8,9,13,15]
idx = -1

binary(arr, 0, len(arr)-1)
print(idx)