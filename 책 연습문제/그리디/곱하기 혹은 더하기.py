# s = "567"
#
# ans = int(s[0])
#
# for x in s[1:]:
#     mul = ans * int(x)
#     plus = ans + int(x)
#     temp = max(mul, plus)
#     if temp <= 2000000000:
#         ans = temp
#
# print(ans)


S = "567"

ans = int(S[0])

for i in S[1:]:
    ans = max(ans + int(i), ans * int(i))

print(ans)


































