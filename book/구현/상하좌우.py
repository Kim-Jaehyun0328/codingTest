N = 5
S = "R R R U D D"

pos = [0, 0]

a = S.split(" ")

for x in a:
    if x == "R" and pos[1] < N-1:
        pos[1] += 1
    elif x == "L" and pos[1] > 0:
        pos[1] -= 1
    elif x == "U" and pos[0] < 0:
        pos[0] -= 1
    elif x == "D" and pos[0] < N-1:
        pos[0] += 1


for x in pos:
    print(x+1, end=" ")
