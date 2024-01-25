def solution(today, terms, privacies):
    answer = []
    dic = dict()
    cnt = 1
    for t in terms:
        k, v = t.split(" ")
        dic[k] = v

    t_year, t_month, t_day = today.split(".")
    t_year, t_month, t_day = int(t_year), int(t_month), int(t_day)
    for privacy in privacies:
        p_year, p_month, p_day = privacy.split(".")
        p_day, p_term = p_day.split(" ")
        p_year, p_month, p_day = int(p_year), int(p_month), int(p_day)

        p_month += int(dic[p_term])
        while p_month > 12:
            p_year += 1
            p_month -= 12

        p_day -= 1
        if p_day == 0:
            p_day = 28
            p_month -= 1
            if p_month == 0:
                p_year -= 1
                p_month = 12

        if t_year > p_year:
            answer.append(cnt)
        elif t_year == p_year and t_month > p_month:
            answer.append(cnt)
        elif t_year == p_year and t_month == p_month and t_day > p_day:
            answer.append(cnt)

        cnt += 1

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))