# def solution(number, k):
#     answer = ''
#     number = list(number)
#
#     for i in range(len(number)):
#         if k == 0:
#             answer += "".join(number[i:])
#             break
#         if (i + k) >= len(number):
#             break
#         for j in range(i + 1, i + 1 + k):
#             if number[j] > number[i]:
#                 k -= 1
#                 break
#         else:
#             answer += number[i]
#
#     if k != 0:
#         for _ in range(k-len(answer)):
#             answer += number.pop()
#
#     return answer

def solution(number, k):
    answer = []

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return "".join(answer[:len(number) - k])

print(solution("4177252841", 4))