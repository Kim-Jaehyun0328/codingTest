def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x))
    dict_ = {}

    for x in phone_book:
        for i in range(1, len(x)):
            if x[0:i] in dict_:
                return False
        else:
            dict_[x] = 1

    return answer


print(solution(["12","123","1235","567","88"]))