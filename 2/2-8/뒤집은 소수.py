import sys
sys.stdin=open("in5.txt", "rt")

def reverse(x):
    a=str(x)
    a = a[::-1]
    return int(a)

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, x//2+1):
            if x%i == 0 :
                return False
        return True

N = int(input())
pList = list(map(int, input().split()))

for i in range(N):
    reverseNum = reverse(pList[i])
    prime = isPrime(reverseNum)
    if prime == True:
        print(reverseNum, end= " ")
