import math


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    s1 = []
    s2 = []

    l1 = 0
    l2 = 0
    while l1 < len(str1) - 1:
        if 97 <= ord(str1[l1]) <= 122:
            if 97 <= ord(str1[l1 + 1]) <= 122:
                s1.append(str1[l1] + str1[l1 + 1])
                l1 += 1
            else:
                l1 += 2
        else:
            l1 += 1

    while l2 < len(str2) - 1:
        if 97 <= ord(str2[l2]) <= 122:
            if 97 <= ord(str2[l2 + 1]) <= 122:
                s2.append(str2[l2] + str2[l2 + 1])
                l2 += 1
            else:
                l2 += 2
        else:
            l2 += 1

    s1.sort()
    s2.sort()



    a = []  # 합집합
    b = []  # 교집합
    x, y = 0, 0  # s1 인덱스 포인터, s2 인덱스 포인터
    while True:
        if x == len(s1):
            for i in range(y, len(s2)):
                a.append(s2[i])
            break
        elif y == len(s2):
            for i in range(x, len(s1)):
                a.append(s1[i])
            break
        if s1[x] == s2[y]:
            a.append(s1[x])
            b.append(s1[x])
            x += 1
            y += 1
        elif s1[x] > s2[y]:
            a.append(s2[y])
            y += 1
        elif s1[x] < s2[y]:
            a.append(s1[x])
            x += 1

    if not b and a:
        return 0
    if not a and not b:
        return 65536

    answer = math.floor(len(b) / len(a) * 65536)

    return answer


print(solution("A+C", "DEF"))