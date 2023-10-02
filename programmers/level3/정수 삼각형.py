#DFS 버전(더 느림)

# answer = 0
#
#
# def solution(triangle):
#     def DFS(L, temp, idx):
#         global answer
#
#         if L == len(triangle):
#             if temp > answer:
#                 answer = temp
#         else:
#             DFS(L + 1, temp + triangle[L][idx], idx)
#             DFS(L + 1, temp + triangle[L][idx + 1], idx + 1)
#
#     DFS(1, triangle[0][0], 0)
#
#     return answer


#DP 버전? (더 빠름)

def solution(triangle):
    dy = [[] for _ in range(len(triangle))]
    dy[0].append(triangle[0][0])
    dy[1].append(triangle[0][0] + triangle[1][0])
    dy[1].append(triangle[0][0] + triangle[1][1])

    for i in range(2, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                dy[i].append(triangle[i][j] + dy[i - 1][0])
            elif j == i:
                dy[i].append(triangle[i][j] + dy[i - 1][i - 1])
            else:
                dy[i].append(max(triangle[i][j] + dy[i - 1][j - 1], triangle[i][j] + dy[i - 1][j]))

    return max(dy[len(dy) - 1])
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))