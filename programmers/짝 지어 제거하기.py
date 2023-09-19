s = "baabaa"
tmp = []
for x in s:
    print(x)
    tmp.append(x)
    if len(tmp) > 1 and tmp[-1] == tmp[-2]:
        tmp.pop()
        tmp.pop()

if len(tmp) == 0:
    print(1)
else:
    print(0)