clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
answer = 1
dict_ = {}

for x in clothes:
    if x[1] in dict_:
        dict_[x[1]].append(x[0])
    else:
        dict_[x[1]] = [x[0]]

for k, v in dict_.items():
    answer *= (len(v)+1)

print(answer-1)