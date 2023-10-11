n= 4
arr = [5, 1, 7, 9]

answer = 0
min_value = int(1e9)
for x in arr:
    distance = 0
    for i in range(len(arr)):
        distance += abs(x-arr[i])
    if distance < min_value:
        min_value = distance
        answer = x
    elif distance == min_value:
        answer = min(answer, x)


print(answer)