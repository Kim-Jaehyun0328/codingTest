N, M, K = 5, 7, 2

l = [3,4,3,4,3]
answer = 0


l.sort(reverse= True)

cnt = 0

for i in range(M):
    if cnt < K:
        answer += l[0]
        cnt += 1
    else:
        cnt = 0
        answer += l[1]
print(answer)