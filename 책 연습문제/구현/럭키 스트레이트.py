s = "123411"
half = len(s) // 2

sum = 0
for i in range(half):
    sum += int(s[i])

for x in s[half:]:
    sum -= int(x)

if sum == 0:
    print("LUCKY")
else:
    print("READY")