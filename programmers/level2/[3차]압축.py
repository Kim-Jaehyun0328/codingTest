def solution(msg):
    answer = []
    dict_ = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11,
             "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21
        , "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    last_num = 27
    temp = ""

    idx = 0
    while idx < len(msg):
        temp += msg[idx]
        while temp in dict_:
            idx += 1
            if idx < len(msg):
                temp += msg[idx]
            else:
                break
        if temp not in dict_:
            dict_[temp] = last_num
            last_num += 1
            temp = temp[0:-1]
        answer.append(dict_[temp])
        temp = ""
    return answer
print(solution("KAKAO"))