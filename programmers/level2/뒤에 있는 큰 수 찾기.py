# def solution(numbers):
#     answer = []

#     temp = sorted(numbers, reverse = True)
#     if temp == numbers:
#         return [-1 for _ in range(len(numbers))]

#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[j] > numbers[i]:
#                 answer.append(numbers[j])
#                 break
#         else:
#             answer.append(-1)

#     return answer


def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer


