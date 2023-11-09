# def solution(numbers):
#     answer = []
#
#     for number in numbers:
#         temp = number
#         s = ""
#         while temp > 0:  # 2진수 구하기
#             div = temp % 2
#             s = str(div) + s
#             temp //= 2
#         while len(s) < 18:  # 앞을 0으로 채우기
#             s = "0" + s
#
#         new = number + 1
#         while True:
#             new_temp = new
#             new_s = ""
#             while new_temp > 0:  # 2진수 구하기
#                 div = new_temp % 2
#                 new_s = str(div) + new_s
#                 new_temp //= 2
#             while len(new_s) < 18:
#                 new_s = "0" + new_s
#             cnt = 0
#             for i in range(len(s)):
#                 if s[i] != new_s[i]:
#                     cnt += 1
#             if cnt <= 2:
#                 answer.append(new)
#                 break
#             new += 1
#
#     return answer
#
# print(solution([3,7]))

def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            s = "0" + bin(number)[2:]
            idx = s.rfind("0")
            s = list(s)
            s[idx] = "1"
            s[idx + 1] = "0"
            s = "".join(s)
            s = int(s, 2)
            answer.append(s)

    return answer

print(solution([2,7]))
