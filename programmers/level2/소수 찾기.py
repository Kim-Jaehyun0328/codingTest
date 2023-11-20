# from itertools import permutations
#
# def solution(numbers):
#     prime = set()
#     for i in range(1, len(numbers) + 1):
#         for number in permutations(numbers, i):
#             num = int("".join(number))
#             if num < 2:
#                 continue
#             temp = num // 2
#             for i in range(2, temp + 1):
#                 if num % i == 0:
#                     break
#             else:
#                 prime.add(num)
#
#     return len(prime)

from itertools import permutations


def solution(numbers):
    prime = set()
    for i in range(1, len(numbers) + 1):
        for number in permutations(numbers, i):
            num = int("".join(number))
            if num < 2:
                continue
            for i in range(2, int((num ** 0.5) + 1)):
                if num % i == 0:
                    break
            else:
                prime.add(num)

    return len(prime)

print(solution("017"))