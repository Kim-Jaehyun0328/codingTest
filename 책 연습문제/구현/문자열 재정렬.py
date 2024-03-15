# s = "AJKDLSI412K4JSJ9D"
# num = 0
# ans = []
# for x in s:
#     if x.isdigit():
#         num += int(x)
#     else:
#         ans.append(x)
# ans.sort()
# ans.append(str(num))
# ans = "".join(ans)
# print(ans)

S = "K1KA5CB7"

temp = []
num = 0
for i in S:
    if i.isalpha():
        temp.append(i)
    else:
        num += int(i)

temp.sort()
temp = "".join(temp)


if num != 0:
    temp += str(num)

print(temp)



























