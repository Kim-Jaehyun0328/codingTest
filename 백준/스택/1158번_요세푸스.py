# N, K = map(int, input().split())
N, K = 7,3
stack = [i+1 for i in range(N)]
ans = []
num = 0
while stack:
    num += K-1
    if num >= len(stack):
        num = num%len(stack)
    ans.append(stack.pop(num))


print(str(ans).replace('[', '<').replace(']', '>'))
