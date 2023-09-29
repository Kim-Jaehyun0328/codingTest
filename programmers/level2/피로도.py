answer = 0


def solution(k, dungeons):
    def DFS(L):
        global answer
        if L == len(dungeons):
            temp = k
            cnt = 0
            for x in res:
                if temp < dungeons[x][0]:
                    break
                else:
                    temp -= dungeons[x][1]
                    cnt += 1
            if cnt > answer:
                answer = cnt
            return
        else:
            for i in range(len(dungeons)):
                if ch[i] == 0:
                    ch[i] = 1
                    res[L] = i
                    DFS(L + 1)
                    ch[i] = 0

    ch = [0 for _ in range(len(dungeons))]
    res = [0 for _ in range(len(dungeons))]
    DFS(0)
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))