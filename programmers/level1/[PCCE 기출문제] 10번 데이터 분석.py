def solution(data, ext, val_ext, sort_by):
    answer = []
    standard = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    for d in data:
        if d[standard[ext]] < val_ext:
            answer.append(d)

    answer = sorted(answer, key=lambda x: x[standard[sort_by]])

    return answer

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))