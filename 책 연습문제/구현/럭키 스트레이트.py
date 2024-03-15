# s = "123411"
# half = len(s) // 2
#
# sum = 0
# for i in range(half):
#     sum += int(s[i])
#
# for x in s[half:]:
#     sum -= int(x)
#
# if sum == 0:
#     print("LUCKY")
# else:
#     print("READY")


N = "123402"

half = len(N)//2



first = sum(int(i) for i in N[:half])
second = sum(int(i) for i in N[half:])


if first == second:
    print("LUCKY")
else:
    print("READY")



































