import sys
from collections import deque

sys.stdin=open("practice2", "r")
input = sys.stdin.readline
N, M, K, X = map(int, input().split())

arr = [[] for _ in range(N+1)]
answer = 0

dist = [-1 for _ in range(N+1)]
dist[X] = 0
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

q = deque([X])


while q:
    now = q.popleft()

    for next_node in arr[now]:
        if dist[next_node] == -1:
            dist[next_node] = dist[now] + 1
            q.append(next_node)


check = False

for i in range(1, N+1):
    if dist[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)


#
# # 최단 거리를 하나씩 확인, k와 일치하면 해당 도시 출력
# import sys
# from collections import deque  # bfs 풀이
# sys.stdin=open("practice2", "r")
#
# input = sys.stdin.readline
# n, m, k, x = map(int, input().split())
#
# g = [[] for i in range(n + 1)]  # n+1개의 노드를 갖는 그래프 생성
#
# for i in range(m):  # 도로 입력받기
#     a, b = map(int, input().split())
#     g[a].append(b)
#
# d = [-1] * (n + 1)  # 노드 간 거리 -1로 초기화
# d[x] = 0  # 시작 노드의 거리는 0으로
#
# q = deque([x])  # 시작 노드
# while q:
#     start = q.popleft()  # 현재 노드 pop
#
#     for nx in g[start]:  # 현재 갈 수 있는 모든 노드 탐색
#         if d[nx] == -1:  # 방문한적 없는 노드이면
#             d[nx] = d[start] + 1  # 방문 처리
#             q.append(nx)
#
# tf = False  # k거리에 해당하는 도시가 있는지 없는지 판별
#
# for i in range(1, n + 1):
#     if d[i] == k:
#         print(i)
#         tf = True  # 있음
#
# if tf == False:  # 없다면 -1
#     print(-1)