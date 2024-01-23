def solution(board, h, w):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if board[nx][ny] == board[h][w]:
                answer += 1

    return answer


print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"],
                ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]],
               1,1))