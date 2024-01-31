def solution(arr):
    if len(arr) == 1:
        return [arr.count(0), arr.count(1)]

    ch = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
    answer = [0, 0]
    length = len(arr)  # 이걸 나누기 2씩 하면서 체크

    while length > 1:
        for i in range(0, len(arr), length):  # 각 꼭지점
            for j in range(0, len(arr), length):
                if ch[i][j] == 1:
                    continue
                flag = False
                for ti in range(i, i+length):
                    for tj in range(j, j+length):
                        if arr[i][j] != arr[ti][tj]:
                            flag = True
                    if flag == True:
                        break
                else:
                    for ti in range(i, i+length):
                        for ty in range(j, j+length):
                            ch[ti][ty] = 1
                    answer[arr[i][j]] += 1
        length //= 2

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if ch[i][j] == -1:
                answer[arr[i][j]] += 1

    return answer

# def solution(arr):
#     def compress(x, y, length):
#         if length == 1:
#             return [0, 1] if arr[x][y] == 1 else [1, 0]
#
#         check_value = arr[x][y]
#         can_compress = True
#
#         for i in range(x, x + length):
#             for j in range(y, y + length):
#                 if arr[i][j] != check_value:
#                     can_compress = False
#                     break
#
#         if can_compress:
#             return [0, 1] if check_value == 1 else [1, 0]
#         else:
#             half_length = length // 2
#             result = [0, 0]
#
#             for i in range(2):
#                 for j in range(2):
#                     result = [x + y for x, y in zip(result, compress(x + i * half_length, y + j * half_length, half_length))]
#             return result
#
#     return compress(0, 0, len(arr))

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))