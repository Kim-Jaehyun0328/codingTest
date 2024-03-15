# import sys
# sys.stdin=open("practice", "r")
#
# n = int(input())
# k = int(input())
# data = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# info = []
#
# for _ in range(k):
#     a, b = map(int, input().split())
#     data[a][b] = 1
# l = int(input())
# for _ in range(l):
#     x, c = input().split()
#     info.append((int(x), c))
#
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
#
#
# def turn(direction, c):
#     if c == "L":
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return direction
#
#
# def simulate():
#     x, y = 1, 1
#     data[x][y] = 2
#     direction = 0
#     time = 0
#     index = 0
#     q = [(x, y)]
#     while True:
#         nx = x + dx[direction]
#         ny = y + dy[direction]
#         if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
#             if data[nx][ny] == 0:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#                 px, py = q.pop(0)
#                 data[px][py] = 0
#             if data[nx][ny] == 1:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#         else:
#             time += 1
#             break
#         x, y = nx, ny
#         time += 1
#         if index < l and time == info[index][0]:
#             direction = turn(direction, info[index][1])
#             index += 1
#     return time
#
#
# print(simulate())


def check(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def solution(key, lock):
    answer = True
    n = len(lock)
    m = len(key)

    new_lock = [[0 for _ in range(n * 3)] for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)

        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return answer

























