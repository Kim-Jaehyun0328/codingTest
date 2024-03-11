from collections import deque

v, e = 7, 8
arr = [[1,2],[1,5],[2,3],[2,6],[3,4],[4,7],[5,6],[6,4]]
indegree = [0 for _ in range(v+1)]

graph = [[] for _ in range(v+1)]
for a,b in arr:
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end= " ")

topology_sort()