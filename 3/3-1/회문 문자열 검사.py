import sys
sys.stdin=open("in4.txt","r")

N = int(input())

for i in range(N):
    a = input().lower()
    if a == a[::-1] :
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
