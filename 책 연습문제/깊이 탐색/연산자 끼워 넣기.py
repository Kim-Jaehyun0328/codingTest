import sys
sys.stdin=open("practice4", "r")
input=sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
min_num = int(1e9)
max_num = -int(1e9)


def dfs(depth, total, plus, minus, mul, div):
    global max_num
    global min_num
    if depth == N:
        if total > max_num:
            max_num = total
        if total < min_num:
            min_num = total
        return
    if plus:
        dfs(depth+1, total+num[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth+1, total-num[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth + 1, total * num[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth + 1, int(total/num[depth]), plus, minus, mul, div-1)



dfs(1, num[0], op[0], op[1], op[2], op[3])

print(max_num)
print(min_num)
