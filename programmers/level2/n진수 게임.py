from collections import deque


def solution(n, t, m, p):
    answer = ''
    q = deque()
    q.append("0")
    q.append("0")
    num = 1

    while len(q) < t * m:
        temp = num
        s = ""
        while temp > 0:
            remain = temp % n
            temp //= n
            if remain == 10:
                remain = "A"
            elif remain == 11:
                remain = "B"
            elif remain == 12:
                remain = "C"
            elif remain == 13:
                remain = "D"
            elif remain == 14:
                remain = "E"
            elif remain == 15:
                remain = "F"
            s = str(remain) + s
        for x in s:
            q.append(x)
        num += 1

    num = p
    for i in range(1, len(q)):
        if len(answer) == t:
            break
        if i == num:
            answer += q[i]
            num += m

    return answer

print(solution(2,4,2,1))