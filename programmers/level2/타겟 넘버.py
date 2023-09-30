answer = 0

def solution(numbers, target):

    def DFS(L, temp):
        global answer
        if L == len(numbers):
            if temp == target:
                answer += 1
            return
        else:
            DFS(L + 1, (temp + numbers[L]))
            DFS(L + 1, temp - numbers[L])
        return

    DFS(0, 0)

    return answer

print(solution([1, 1, 1, 1, 1], 3))

