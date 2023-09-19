id_list= ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2

answer = [0 for _ in range(len(id_list))]
from_id = {key: [] for key in id_list}
to_id = {key: 0 for key in id_list}

report = set(report)
report = list(report)
for i in range(len(report)):
    from_, to = report[i].split()
    from_id[from_].append(to)
    to_id[to] += 1

for key, value in to_id.items(): #신고당한사람
    if value >= k:
        i = 0
        for key2, value2 in from_id.items():
            print(key2, value2)
            if key in from_id[key2]:
                answer[i] += 1
            i+=1

print(answer)