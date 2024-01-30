def solution(m, n, board):
    answer = 0
    ch = [[-1 for _ in range(n)] for _ in range(m)]
    dx = [0, 1, 1]
    dy = [1, 1, 0]
    for i in range(len(board)):
        board[i] = list(board[i])

    while True:
        flag = False
        for i in range(len(board) - 1):
            for j in range(len(board[0]) - 1):
                for k in range(3):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if board[i][j] == 'XX' or board[i][j] != board[nx][ny]:
                        break
                else:  # 현재 기준 2X2가 모두 같다면 ch배열에서 1로 체크, board 배열에는 0으로 변경
                    flag = True
                    ch[i][j] = 1
                    for k in range(3):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        ch[nx][ny] = 1
        if flag == False:  # 더 이상 사라지는 것이 없다면
            break

        for i in range(len(ch)):
            for j in range(len(ch[0])):
                if ch[i][j] == 1:  # 없어져야 할 배열이라면
                    board[i][j] = 'XX'
                    answer += 1
                    ch[i][j] = -1  # 다시 -1으로 초기화

        for j in range(len(board[0])):
            for i in range(len(board)):
                for ii in range(1, len(board)-i):
                    if board[ii][j] == 'XX':
                        board[ii-1][j], board[ii][j] = board[ii][j], board[ii-1][j]

        for i in range(len(board)):
            print(board[i])
        print("========================")

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))