def solution(s):
    answer = ''
    dict_ = {key: 0 for key in 'abcdefghijklmnopqrstuvwxyz'}
    temp = []
    for i in s:
        dict_[i] += 1

    for i in s:
        if dict_[i] == 1:
            temp.append(i)
    answer = ''.join(sorted(temp))
    return answer

#s = "abcabcadc"