from collections import Counter


def solution(want, number, discount):
    answer = 0
    dict_ = {}

    for w, n in zip(want, number):
        dict_[w] = n

    for i in range(0, len(discount) - 9):
        temp = discount[i:10 + i]
        ch = Counter(temp)
        if dict_ == ch:
            answer += 1

    # temp = []
    # number_temp = number
    # prev = want[0]
    # for i in range(0, len(discount)):
    #     if discount[i] not in want: #want에 없는 품목을 만나면 리셋
    #         number_temp = number
    #         temp.clear()
    #         continue
    #     else:
    #         if len(temp) != 10:
    #             temp.append(discount[i])
    #             number_temp[want.index(discount[i])] -= 1
    #         else:
    #             prev = temp.pop(0)
    #             number_temp[want.index(prev)] += 1
    #             temp.append(discount[i])
    #             number_temp[want.index(discount[i])] -= 1
    #             if number_temp.count(0) == len(number):
    #                 answer += 1

    return answer