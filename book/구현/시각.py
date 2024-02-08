# N = 5
#
# answer = 0
# for i in range(N+1):
#     for j in range(60):
#         for k in range(60):
#             hour = str(i)
#             minute = str(j)
#             second = str(k)
#             if "3" in second or "3" in minute or "3" in hour:
#                 answer += 1
#
#
# print(answer)


n = 5
answer = 0
for h in range(n+1):
    if "3" in str(h):
        answer += 60*60
        continue
    for m in range(60):
        if "3" in str(m):
            answer += 60
            continue
        for s in range(60):
            if "3" in str(s):
                answer += 1
# for h in range(n+1):
#     for m in range(60):
#         for s in range(60):
#             if "3" in str(h) or "3" in str(m) or "3" in str(s):
#                 answer+=1

print(answer)










