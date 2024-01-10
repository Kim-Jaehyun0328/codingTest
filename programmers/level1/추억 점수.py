#zip() 내장 함수를 사용하면 한 줄로 딕셔너리 만들기 가능하다.

def solution(names, yearning, photos):
    answer = []

    # dic = {n:y for n, y in name,yearning}

    dic = dict()

    for i in range(len(names)):
        dic[names[i]] = yearning[i]

    for photo in photos:
        point = 0
        for name in photo:
            if name not in dic:
                continue
            else:
                point += dic[name]
        answer.append(point)

    return answer

print(solution(["may", "kein", "kain", "radi"], [5,10,1,3],
               [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))