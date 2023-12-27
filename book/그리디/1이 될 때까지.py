# N, K = 25, 5
# answer = 0
#
#
# while N != 1 and N > 1:
#     if N%K == 0:
#         N //= K
#         answer += 1
#     else:
#         N -= 1
#         answer += 1
#
# print(answer)

n, k = 25, 3
ans = 0

while n != 1:
    if n%k == 0:
        n //= k
        ans += 1
    else:
        n -= 1
        ans += 1
print(ans)