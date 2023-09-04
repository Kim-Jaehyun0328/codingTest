import sys
sys.stdin=open("practice", "r")


def DFS(L, sum):
    global res
    print(sum)
    if sum > money:
        return
    if L == coin_case:
        if sum == money:
            res += 1
    else:
        for i in range(coin_num[L]+1):
            DFS(L+1, sum+(coin[L]*i))

if __name__ == "__main__":
    money = int(input())
    coin_case = int(input())
    coin = []
    coin_num = []
    for i in range(coin_case):
        a, b = map(int, input().split())
        coin.append(a)
        coin_num.append(b)
    res = 0
    DFS(0, 0)
    print(res)
