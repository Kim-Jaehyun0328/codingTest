def solution(n, computers):
    parents = [i for i in range(n)]

    def find(a):
        if parents[a] == a:
            return a
        parents[a] = find(parents[a])
        return parents[a]

    def union(a, b):
        aP = find(a)
        bP = find(b)

        if aP < bP:
            parents[bP] = aP
        else:
            parents[aP] = bP

    for row in range(n):
        for col in range(row):
            if row == col:
                continue

            if computers[row][col]:
                union(row, col)

    ans1 = set()
    ans2 = set(parents)
    for i in range(n):
        ans1.add(find(parents[i]))
    return len(ans1)

print(solution(5, [[1, 0, 0, 0, 1], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]))