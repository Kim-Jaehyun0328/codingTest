def solution(land):
    for i in range(1, len(land)):  # 행
        for j in range(4):  # 열
            arr = []
            for k in range(4):  # 최대값 구하기
                if j == k:
                    continue
                arr.append(land[i - 1][k] + land[i][j])
            land[i][j] = max(arr)

    return max(land[len(land) - 1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))