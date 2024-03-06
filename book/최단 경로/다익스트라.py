# n, m = 6, 11
# start = 1
# temp = [[1,2,2],[1,3,5],[1,4,1],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],[5,6,2]]
# graph = [[] for _ in range(n+1)]
#
# for a,b,c in temp:
#     graph[a].append((b,c))
#
# print(graph)
#
# visited = [False for _ in range(n+1)]
# distance = [int(1e9) for _ in range(n+1)]
#
#
# def get_smallest_node():
#     min_val = int(1e9)
#     idx = 0
#     for i in range(1, n+1):
#         if distance[i] < min_val and not visited[i]:  #방문하지 않았고, 최단 경로라면
#             min_val = distance[i]
#             idx = i
#     return idx
#
#
# def dijkstra(start):
#     visited[start] = True
#     distance[start] = 0
#
#     for i in graph[start]:
#         distance[i[0]] = i[1]
#
#     for j in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#
#         for k in graph[now]:
#             cost = distance[now] + k[1]
#             if cost < distance[k[0]]:
#                 distance[k[0]] = cost
#
#
#
# dijkstra(start)
#
# for i in range(1, n+1):
#     if distance[i] == int(1e9):
#         print("INFINITY")
#     else:
#         print(distance[i])

import heapq

n, m = 6, 11
start = 1
temp = [[1,2,2],[1,3,5],[1,4,1],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],[5,6,2]]
graph = [[] for _ in range(n+1)]
for a,b,c in temp:
    graph[a].append((b,c))
distance = [int(1e9) for _ in range(n+1)]


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == int(1e9):
        print("INFINITY")
    else:
        print(distance[i])


























