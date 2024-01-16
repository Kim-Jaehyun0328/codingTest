# def solution(number, limit, power):
#     answer = 1  # 숫자 1을 포함 시켜서 시작
#
#     for num in range(2, number + 1):
#         cnt = 2  # 1과 자기 자신은 누구에게나 약수
#         for j in range(2, num // 2 + 1):
#             if num % j == 0:
#                 cnt += 1
#
#         if cnt > limit:
#             answer += power
#         else:
#             answer += cnt
#
#     return answer
# print(solution(5,3,2))

# def solution(number, limit, power):
#     answer = 1  # 숫자 1을 포함 시켜서 시작
#     flag = False
#     for num in range(2, number + 1):
#         cnt = 2  # 1과 자기 자신은 누구에게나 약수
#         flag = False
#         for j in range(2, num // 2 + 1):
#             if num % j == 0:
#                 cnt += 1
#             if cnt > limit:
#                 answer += power
#                 flag = True
#                 break
#         if flag == False:
#             answer += cnt
#
#     return answer

# def solution(number, limit, power):
#     answer = 1 #숫자 1을 포함 시켜서 시작
#     flag = False
#     for num in range(2, number+1):
#         cnt = 2 #1과 자기 자신은 누구에게나 약수
#         flag = False
#         for j in range(2, num//2+1):
#             if num%j == 0:
#                 cnt += 1
#             if cnt > limit:
#                 answer += power
#                 flag = True
#                 break
#         if flag == False:
#             answer += cnt


#     return answer

import math


def solution(number, limit, power):
    answer = 1  # 숫자 1을 포함 시켜서 시작
    for num in range(2, number + 1):
        cnt = 2  # 1과 자기 자신은 누구에게나 약수
        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                cnt += 2
            if j * j == num:
                cnt -= 1
        if cnt > limit:
            answer += power
        else:
            answer += cnt

    return answer

print(solution(5,3,2))
