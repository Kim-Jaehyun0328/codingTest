# import heapq
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)  # 거리, 노드
#
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:  # 노드, 거리
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
#     return
#
#
# INF = int(1e9)
# N, M, C = 3, 2, 1
# graph = [[] for _ in range(N + 1)]
# graph[1].append((3, 2))
# graph[1].append((2, 4))
# distance = [INF for _ in range(N + 1)]
#
# start = C
# dijkstra(start)
#
# cities = 0
# times = 0
# for x in distance[1:]:
#     if x != 0 and x != INF:
#         cities += 1
# print(cities, max(distance[1:]))

import heapq

INF = int(1e9)
N, M, C = 3, 2, 1
arr = [[1,2,4],[1,3,2]]
distance = [INF for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for a, b, c in arr:
    graph[a].append((b, c))

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
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(C)

cnt = 0
max_val = 0


for d in distance:
    if d != INF:
        cnt += 1
        max_val = max(max_val, d)
print(cnt-1, max_val)

















