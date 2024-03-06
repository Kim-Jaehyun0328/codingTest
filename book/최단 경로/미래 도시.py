# INF = int(1e9)
# X, K = 3, 4
# N, M = 5, 7
# graph = [[0 for _ in range(N)] for _ in range(N)]
# a = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [4, 5], [4, 5]]
#
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             graph[i][j] = 0
#         else:
#             graph[i][j] = INF
#
# for x in a:
#     graph[x[0] - 1][x[1] - 1] = 1
#     graph[x[1] - 1][x[0] - 1] = 1
#
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             graph[i][j] = min(graph[i][j], (graph[i][k] + graph[k][j]))
#
# if graph[X][K] == INF:
#     print(-1)
#
# print(graph[0][K] + graph[K][X])


INF = int(1e9)
X, K = 4, 5
N, M = 5, 7
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
a = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [3, 5], [4, 5]]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for i in a:
    graph[i[0]][i[1]] = 1
    graph[i[1]][i[0]] = 1



for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in graph:
    print(i[1:])

print(graph[1][K], graph[K][X])










