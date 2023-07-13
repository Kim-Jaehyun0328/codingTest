gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
answer = []
temp = sorted(list(set(gems)))

res = 100000
startRes, endRes = 0, 0
for i in range(len(gems)):
    temp2 = set()
    for j in range(i, len(gems)):
        temp2.add(gems[j])
        if len(temp) == len(temp2):
            start, end = i + 1, j + 1
            num = end - start
            break
    if res > num:
        res = num
        startRes = start
        endRes = end

answer.append(startRes)
answer.append(endRes)


