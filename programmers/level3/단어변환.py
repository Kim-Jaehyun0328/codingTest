answer = 1e9


def solution(begin, target, words):
    global answer
    if target not in words:
        return 0
    length = len(begin)
    ch = [0 for _ in range(len(words))]

    def DFS(L, word, cnt):
        global answer
        if word == target:
            if cnt < answer:
                answer = cnt
        else:
            for x in words:
                count = 0
                for j in range(length):
                    if word[j] == x[j]:
                        count += 1
                if count == (length - 1):
                    if ch[words.index(x)] == 0:
                        ch[words.index(x)] = 1
                        DFS(words.index(x) + 1, x, cnt + 1)
                        ch[words.index(x)] = 0
        return

    for i in range(len(words)):
        cnt = 0
        for j in range(length):
            if begin[j] == words[i][j]:
                cnt += 1
        if cnt == (length - 1):
            if ch[i] == 0:
                ch[i] = 1
                DFS(i + 1, words[i], 1)
                ch[i] = 0

    return answer

print(solution("aoa", "aof", ["aob", "aoc", "aod", "aof", "aoe"]))