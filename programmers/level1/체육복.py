def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    for x in reserve[:]:
        if x in lost:
            reserve.remove(x)
            lost.remove(x)

    for x in reserve:
        if x - 1 in lost:
            lost.remove(x - 1)
        elif x + 1 in lost:
            lost.remove(x + 1)

    return n - len(lost)

print(solution(5, [4,2], [5,3]))
