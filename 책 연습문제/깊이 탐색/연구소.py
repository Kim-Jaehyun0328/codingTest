n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i].append(list(map(int,input().split())))

arr.sort(key=lambda x:x[1], reverese=True)