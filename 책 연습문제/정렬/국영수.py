import sys
sys.stdin=open("practice", "r")
n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())


arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for x in arr:
    print(x[0])