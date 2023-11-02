def solution(n):
    temp1 = 1
    temp2 = 2

    for i in range(3, n + 1):
        now = temp1 + temp2
        temp1, temp2 = temp2, now

    return now % 1000000007

print(solution(5))