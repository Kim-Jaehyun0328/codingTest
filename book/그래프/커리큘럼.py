import copy
import sys
from collections import deque

sys.stdin = open("practice3", "r")

N = int(input())

indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
time = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)]
for i in range(1,N+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    for j in temp[1:]:
        if j == -1:
            break
        graph[j].append(i)
        indegree[i] += 1


def topology_sort():
    result = copy.deepcopy(time)
    print(result)
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in range(1, N + 1):
        print(result[i])

topology_sort()
