import sys
sys.stdin= open("in5.txt", "rt")
T = int(input())

for i in range(T):
    n, s, e, k = map(int, input().split())
    a=list(map(int, input().split()))
    temp = a[s-1:e]
    temp.sort()
    print("#%d %d" %(i+1, temp[k-1]))