from itertools import permutations


# def solution(numbers):
#     answer = -1e9
#     temp = 0
#     for number in permutations(numbers, len(numbers)):
#         temp = int("".join(map(str, number)))
#         if temp > answer:
#             answer = temp
#
#     return str(answer)

# def solution(numbers):
#     answer = ''
#     hash_list = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
#
#     for number in numbers:
#         hash_list[int(str(number)[0])].append(str(number))
#
#     for number in range(9, -1, -1):
#         max_num = str(-1e9)
#         temp = ""
#         for a in permutations(hash_list[number], len(hash_list[number])):
#             temp = "".join(a)
#             if temp > max_num:
#                 max_num = temp
#         if max_num != str(-1e9):
#             answer += max_num
#
#     return answer

def solution(numbers):
    answer = ''
    str_list = [str(i) for i in numbers]
    str_list.sort(key=lambda num: num * 3, reverse=True)

    return str(int("".join(str_list)))

print(solution([6, 10, 2]))