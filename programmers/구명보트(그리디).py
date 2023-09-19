# people = [70, 50, 80, 50]
# limit = 100
# answer = 0
#
# people.sort(reverse= True)
# ch = [0 for _ in range(len(people))]
# for i in range(len(people)):
#     if ch[i] == 0:
#         ch[i] = 1
#         temp = limit - people[i]
#         for j in range(i + 1, len(people)):
#             if ch[j] == 0:
#                 if people[j] <= temp:
#                     ch[j] = 1
#                     break
#         answer += 1
#         print(ch)
#
# print(answer)

from collections import deque

people = [70, 50, 80, 50]
limit = 100
answer = 0

dq = deque(sorted(people))

while dq:
    if len(dq) == 1:
        answer += 1
        break
    else:
        if dq[0] + dq[-1] <= limit:
            dq.pop()
            dq.popleft()
            answer += 1
        else:
            dq.pop()
            answer += 1

print(answer)