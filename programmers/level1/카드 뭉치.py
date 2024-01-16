from collections import deque


def solution(cards1, cards2, goal):
    flag = True
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for x in goal:
        if len(cards1) != 0 and cards1[0] == x:
            cards1.popleft()
            continue
        elif len(cards2) != 0 and cards2[0] == x:
            cards2.popleft()
            continue
        flag = False

    if flag:
        return "Yes"
    return "No"

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))