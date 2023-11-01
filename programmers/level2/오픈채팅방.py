def solution(record):
    answer = []
    id_list = {}
    for x in record:
        arr = x.split(" ")
        if arr[0] == "Enter":
            id_list[arr[1]] = arr[2]
            answer.append((arr[0], arr[1]))
        elif arr[0] == "Change":
            id_list[arr[1]] = arr[2]
        elif arr[0] == "Leave":
            answer.append((arr[0], arr[1]))  # leave, id 저장

    for i in range(len(answer)):
        if answer[i][0] == "Leave":
            answer[i] = str(id_list[answer[i][1]]) + "님이 나갔습니다."
        if answer[i][0] == "Enter":
            answer[i] = str(id_list[answer[i][1]]) + "님이 들어왔습니다."

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))