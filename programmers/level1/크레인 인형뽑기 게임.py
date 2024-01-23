def solution(board, moves):
    answer = 0
    length = len(board)
    bucket = []
    for i in moves:
        idx = i - 1
        for j in range(0, length):
            if board[j][idx] != 0:
                bucket.append(board[j][idx])
                board[j][idx] = 0
                break
        if len(bucket) > 1 and bucket[-1] == bucket[-2]:
            bucket.pop()
            bucket.pop()
            answer += 2

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
               [1,5,3,5,1,2,1,4]))