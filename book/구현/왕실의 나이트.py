n = "c2"

a = ["a", "b", "c", "d", "e", "f", "g", "h"]


answer = 0

pos = [[-2,-1], [-2, 1], [2, -1], [2,1], [-1,2], [1,2], [-1,-2], [1,-2]]

row = int(n[1])-1
column = a.index(n[0])


for x in pos:
    if 0 <= row + x[0] < 8 and 0 <= column + x[1] < 8:
        answer += 1

print(answer)