n, left, right = 3, 2, 5

answer = []
while left <= right:
        row, column = left//n, left%n
        if column <= row:
            answer.append((row+1))
        else:
            answer.append((row+1) + (column-row))
        left += 1

print(answer)
