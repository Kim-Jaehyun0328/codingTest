s = "0001100"

arr_0 = 0
arr_1 = 0

temp = s[0]
for x in s[1:]:
    if x != temp:
        if temp == "0":
            arr_0 += 1
        else:
            arr_1 += 1
        temp = x
if temp == "0":
    arr_0 += 1
else:
    arr_1 += 1

print(min(arr_0, arr_1))