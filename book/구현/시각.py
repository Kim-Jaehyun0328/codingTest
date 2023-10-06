N = 5

answer = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            hour = str(i)
            minute = str(j)
            second = str(k)
            if "3" in second or "3" in minute or "3" in hour:
                answer += 1


print(answer)