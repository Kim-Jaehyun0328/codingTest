def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10

        if remainder < 5:  # 현재 자리수가 0이상 4이하일 때
            answer += remainder
        elif 5 < remainder:  # 현재 자리수가 5이상 9이하일 때
            answer += (10 - remainder)
            storey += (10 - remainder)
        else:  # 현재 자리수가 5일 때
            if (storey // 10) % 10 > 4:
                answer += remainder
                storey += (10 - remainder)
            else:
                answer += remainder
        storey //= 10
    return answer

print(solution(16))