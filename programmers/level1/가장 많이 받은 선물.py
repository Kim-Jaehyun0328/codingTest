def solution(friends, gifts):
    answer = -int(1e9)
    arr = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    dic = {key: 0 for key in friends}

    for gift in gifts:
        g, t = gift.split(" ")
        dic[g] += 1
        dic[t] -= 1
        arr[friends.index(g)][friends.index(t)] += 1

    for friend in friends:
        temp = 0
        for to in friends:
            if friend == to:
                continue
            if arr[friends.index(friend)][friends.index(to)] > arr[friends.index(to)][friends.index(friend)]:
                temp += 1
            elif arr[friends.index(friend)][friends.index(to)] == arr[friends.index(to)][friends.index(friend)]:
                if dic[friend] > dic[to]:
                    temp += 1
        if temp > answer:
            answer = temp

    return answer




print(solution(["muzi", "ryan", "frodo", "neo"],
               ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))