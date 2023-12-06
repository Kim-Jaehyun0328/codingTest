def solution(maps):
    answer = []
    visited = []
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    q = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            cnt = 0
            if maps[i][j].isdigit() and (i,j) not in visited:
                q.append((i,j))
                visited.append((i,j))
                cnt += int(maps[i][j])
                while q:
                    x, y = q.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny].isdigit() and (nx,ny) not in visited:
                            cnt += int(maps[nx][ny])
                            q.append((nx,ny))
                            visited.append((nx,ny))
                answer.append(cnt)
    answer.sort()
    if not answer:
        return [-1]
    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))