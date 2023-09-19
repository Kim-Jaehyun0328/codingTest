s="one4seveneight"
answer = 0
res = []
pList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num = 1
for i in range(len(s)):
    num -= 1
    if num == 0:
        if s[i] == 'z':  # zero
            res.append(0)
            num = 4
        elif s[i] == 'o':  # one
            res.append(1)
            num = 3
        elif s[i] == 't' and s[i + 1] == 'w':  # two
            res.append(2)
            num = 3
        elif s[i] == 't' and s[i + 1] == 'h':  # three
            res.append(3)
            num = 5
        elif s[i] == 'f' and s[i + 1] == 'o':  # four
            res.append(4)
            num = 4
        elif s[i] == 'f' and s[i + 1] == 'i':  # five
            res.append(5)
            num = 4
        elif s[i] == 's' and s[i + 1] == 'i':  # six
            res.append(6)
            num = 3
        elif s[i] == 's' and s[i + 1] == 'e':  # seven
            res.append(7)
            num = 5
        elif s[i] == 'e':  # eight
            res.append(8)
            num = 5
        elif s[i] == 'n':  # nine
            res.append(9)
            num = 4
        else:
            res.append(s[i])
            num = 1
answer = int(''.join(map(str, res)))
print(answer)