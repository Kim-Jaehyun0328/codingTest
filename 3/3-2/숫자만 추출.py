import sys
sys.stdin = open("in5.txt", "r")

str_ = input()
temp = ""
for i in str_:
    if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') : #if i.isdecimal(): res = res*10+int(x)
        continue
    else:
        temp += i
temp = int(temp)
cnt = 0
for i in range(1, temp+1):
    if temp%i == 0 :
        cnt += 1
print(temp)
print(cnt)