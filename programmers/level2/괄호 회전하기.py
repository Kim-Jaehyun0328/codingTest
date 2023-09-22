from collections import deque

s = "}[](){"

answer = 0

for _ in range(len(s)):
    if s[0] == "(" or s[0] == "[" or s[0] == "{":
        for i in range(1, len(s)):
            if s[i] == ")" and "(" not in s[0:i]:
                break
            if s[i] == "]" and "[" not in s[0:i]:
                break
            if s[i] == "}" and "{" not in s[0:i]:
                break
        else:
            answer += 1

    s = s[1:] + s[0]

print(answer)