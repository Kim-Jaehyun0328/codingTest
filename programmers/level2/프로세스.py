def solution(priorities, location):
    answer = 0
    idx = 0
    l = len(priorities)
    while True:
        if priorities[idx] == max(priorities[idx:]):
            if idx%l == location:
                return answer+1
            idx += 1
            answer += 1
            priorities.append(0)
        else:
            priorities.append(priorities[idx])
            idx += 1

    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))