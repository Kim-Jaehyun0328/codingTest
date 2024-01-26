def solution(players, callings):
    dic = {player: i for i, player in enumerate(players)}

    for c in callings:
        idx = dic[c]
        dic[c] -= 1  # 등 수 추월
        dic[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))