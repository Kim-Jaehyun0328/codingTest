s = "abcabcabcabcdededededede"

answer = len(s)

for step in range(1, len(s) // 2 + 1):
    temp = ""
    previous = s[0:step]
    cnt = 1

    for j in range(step, len(s), step):
        if previous == s[j:step + j]:
            cnt += 1
        else:
            temp += str(cnt) + previous if cnt >= 2 else previous
            cnt = 1
            previous = s[j:step + j]
    temp += str(cnt) + previous if cnt >= 2 else previous
    answer = min(answer, len(temp))

print(answer)
