s1 = "ACBABCBAB"
s2 = "CBBBAB"
ans = -1e9
def DFS(x, y, cnt, temp):
    print(cnt, temp)
    global ans
    for i in range(x+1, len(s1)):
        for j in range(y+1, len(s2)):
            if s1[i] == s2[j]:
                temp += s1[i]
                DFS(i, j, cnt+1, temp)
    if cnt > ans:
        ans = cnt
    return



for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            DFS(i, j, 1, s1[i])


print(ans)