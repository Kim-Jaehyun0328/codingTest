# cnt = 0

# def solution(word):
#     dict_ = {}
#     def DFS(w):
#         global cnt
#         if len(w) > 5:
#             return
#         else:
#             dict_[w] = cnt
#             cnt += 1
#             for x in l:
#                 if len(w+x) > 5:
#                     return
#                 DFS(w+x)
#     l = "AEIOU"
#     DFS("")


#     return dict_[word]


from itertools import product


def solution(word):
    lst = []
    for i in range(1, 6):
        for pro in product(["A", "E", "I", "O", "U"], repeat=i):
            lst.append("".join(pro))

    lst.sort()
    return lst.index(word) + 1



print(solution("AAAAE"))