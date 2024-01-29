def solution(bandage, health, attacks):
    max_num = health
    cnt = 0

    for i in range(attacks[-1][0] + 1):
        if i == attacks[0][0]:  # 몬스터의 공격이 들어옴
            health -= attacks[0][1]
            cnt = 0
            attacks.pop(0)
            if health <= 0:  # 체력이 0 이하라면
                return -1
            continue

        cnt += 1
        if cnt == bandage[0]:
            if health + bandage[2] + bandage[1] > max_num:
                health = max_num
            else:
                health += bandage[2] + bandage[1]
            cnt = 0
        else:
            if health + bandage[1] > max_num:
                health = max_num
            else:
                health += bandage[1]

    return health

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))