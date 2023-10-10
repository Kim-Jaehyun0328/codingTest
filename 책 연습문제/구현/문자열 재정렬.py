s = "AJKDLSI412K4JSJ9D"
num = 0
ans = []
for x in s:
    if x.isdigit():
        num += int(x)
    else:
        ans.append(x)
ans.sort()
ans.append(str(num))
ans = "".join(ans)
print(ans)