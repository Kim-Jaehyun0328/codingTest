citations = [3, 0, 6, 1, 5]

answer = 0

citations.sort()

citations.sort()
n = len(citations)

for i in citations:
    if i >= n:
        break
    else:
        n -= 1
answer = n

print(answer)
