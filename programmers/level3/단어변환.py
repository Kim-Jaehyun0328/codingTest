answer = 1e9

def solution(begin, target, words):
    global answer
    if target not in words:
        return 0
    length = len(begin)
    ch = [0 for _ in range(len(words))]

    def DFS(word, cnt):
        global answer
        if word == target:
            if cnt < answer:
                answer = cnt
        else:
            for i in range(len(words)):
                count = 0
                for j in range(length):
                    if word[j] == words[i][j]:
                        count += 1
                if count == (length - 1):
                    if ch[i] == 0:
                        ch[i] = 1
                        DFS(words[i], cnt + 1)
                        ch[i] = 0

    for i in range(len(words)):
        cnt = 0
        for j in range(length):
            if begin[j] == words[i][j]:
                cnt += 1
        if cnt == (length - 1):
            if ch[i] == 0:
                ch[i] = 1
                DFS(words[i], 1)
                ch[i] = 0
    return answer

print(solution("aoa", "aof", ["aob", "aoc", "aod", "aof", "aoe"]))