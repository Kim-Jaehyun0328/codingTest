import sys
sys.stdin=open("practice", "r")

num, n = map(int, input().split())

# num = list(str(num))
# cnt = 0

# while True:
#     for i in range(len(num)-1):
#         if num[i] < num[i+1]:
#             num.pop(i)
#             cnt += 1
#             break
#     else:
#         num.pop()
#         cnt += 1
#
#     if cnt == n:
#         break
#
# for i in num:
#     print(i, end="")

num = list(map(int, str(num)))

stack = []
for i in num:
    while stack and n > 0 and stack[-1] < i:
        stack.pop()
        n -= 1
    stack.append(i)


if n != 0:
    stack = stack[:-n]

res = ''.join(map(str, stack))
print(res)
