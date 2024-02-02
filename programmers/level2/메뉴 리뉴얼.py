from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        dic = {}
        for order in orders:
            for j in combinations(order, c):
                menu = "".join(sorted(j))
                if menu in dic:
                    dic[menu] += 1
                else:
                    dic[menu] = 1

        if len(dic.keys()) > 0:
            max_num = max(dic.values())
            if max_num > 1:
                for key, value in dic.items():
                    if value == max_num:
                        answer.append(key)

    answer.sort()

    return answer

# from itertools import combinations
#
#
# def solution(orders, course):
#     answer = []
#
#     for course_item in course:
#         comb_count = {}
#         order_combinations = []
#
#         max_order = []
#         for order in orders:
#             order_comb = combinations(list(order), course_item)
#
#             for order in order_comb:
#                 order_comb_string = "".join(sorted(order))
#
#                 if comb_count.get(order_comb_string):
#                     comb_count[order_comb_string] += 1
#
#                 else:
#                     comb_count[order_comb_string] = 1
#
#         max_order = [k for k, v in comb_count.items() if ((v == max(comb_count.values())) and v >= 2)]
#
#         answer.extend(max_order)
#
#     answer = sorted(answer)
#
#     return answer
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))