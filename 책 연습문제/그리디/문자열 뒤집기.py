# s = "0001100"
#
# arr_0 = 0
# arr_1 = 0
#
# temp = s[0]
# for x in s[1:]:
#     if x != temp:
#         if temp == "0":
#             arr_0 += 1
#         else:
#             arr_1 += 1
#         temp = x
# if temp == "0":
#     arr_0 += 1
# else:
#     arr_1 += 1
#
# print(min(arr_0, arr_1))



S = "0001100"

zero_cnt = 0
one_cnt = 0
temp = S[0]
for i in S[1:]:
    if temp != i: #바뀜
        if temp == "0":
            zero_cnt += 1
        else:
            one_cnt += 1
        temp = i

print(min(zero_cnt, one_cnt))






















