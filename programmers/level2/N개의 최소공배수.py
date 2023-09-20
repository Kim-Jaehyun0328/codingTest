arr = [2, 6, 8, 14]

answer = 0
max_num = max(arr)
temp = max_num
flag = True
cnt = 1
while True:
    flag = True
    for x in arr:
        if temp % x != 0:
            flag = False
            break
    if flag == True:
        answer = temp
        break
    cnt += 1
    temp = max_num * cnt



print(answer)