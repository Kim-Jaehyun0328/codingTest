import sys
sys.stdin=open("in2.txt", "r")

n = int(input())
a = [0 for _ in range(n+1)]
a[1] = 1
a[2] = 2

for i in range(3, n+1):
    a[i] = a[i-1] + a[i-2]

print(a[n])