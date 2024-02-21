arr = [0,1,2,3,4,5,6,7,8,9]

cnt = 0
def binary_search(arr, target, start, end):

    if start > end:
        return None

    global cnt
    mid = (start+end)//2

    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        cnt += 1
        binary_search(arr, target, mid+1, end)
    else:
        cnt += 1
        binary_search(arr, target, start, mid-1)



print(binary_search(arr, 8, 0, len(arr)-1))