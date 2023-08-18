import sys
sys.stdin = open("in5.txt", "r")

a = input()

stack = []
res = 0
cnt = 0
# for i in range(len(a)):
#     while stack:
#         if stack[-1] == "(" and a[i] == ")": #레이저
#             res += cnt
#         elif stack[-1] == "(" and a[i] == "(":
#             cnt += 1
#         elif stack[-1] == ")" and a[i] == ")":
#             cnt -= 1
#             res += 1
#
#         break
#     stack.append(a[i])

for i in range(len(a)):
    if stack and a[i] == ")" and a[i-1] == "(":
        stack.pop()
        res += len(stack)
        continue
    elif stack and a[i] == ")" and a[i-1] == ")":
        stack.pop()
        res += 1
        continue
    stack.append(a[i])

print(res)