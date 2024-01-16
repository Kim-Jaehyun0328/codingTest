from itertools import combinations


def solution(nums):
    answer = 0

    for x in combinations(nums, 3):
        num = sum(x)
        for i in range(2, num // 2):
            if num % i == 0:
                break
        else:
            answer += 1

    return answer

print(solution([1,2,3,4]))