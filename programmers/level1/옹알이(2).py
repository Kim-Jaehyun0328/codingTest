def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for babble in babbling:
        temp = babble
        for word in words:
            if word * 2 not in babble:
                babble = babble.replace(word, " ")
        babble = babble.replace(" ", "")
        if babble == "":
            print(temp)
            answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa"]))