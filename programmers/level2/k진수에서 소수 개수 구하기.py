def solution(n, k):
    answer = 0
    dict_ = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
             10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    s = ""
    while n > 0:
        s += dict_[n % k]
        n //= k

    s = (s[::-1])
    idx = 0
    temp = s.split("0")

    for x in temp:
        if x == "" or x == "1":
            continue
        elif x == "2":
            answer += 1
        else:
            x = int(x)
            for i in range(2, int(x ** (1 / 2) + 1)):
                if x % i == 0:
                    break
            else:
                answer += 1

    return answer

print(solution(437674, 3))