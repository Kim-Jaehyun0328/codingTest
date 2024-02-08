# n = "c2"
#
# a = ["a", "b", "c", "d", "e", "f", "g", "h"]
#
#
# answer = 0
#
# pos = [[-2,-1], [-2, 1], [2, -1], [2,1], [-1,2], [1,2], [-1,-2], [1,-2]]
#
# row = int(n[1])-1
# column = a.index(n[0])
#
#
# for x in pos:
#     if 0 <= row + x[0] < 8 and 0 <= column + x[1] < 8:
#         answer += 1
#
# print(answer)


#8X8 체스판
# inp = "a1"
# pos = [ord(inp[0])-97, int(inp[1])-1] # ord("a") == 97
# nx = [-2,-2,-1,1,2,2,-1,1]
# ny = [-1,1,2,2,-1,1,-2,-2]
# ans = 0
# for i in range(8):
#     dx = nx[i] + pos[0]
#     dy = ny[i] + pos[1]
#     if 0<=dx<8 and 0<=dy<8:
#         ans += 1
# print(ans)



answer = 0
pos = "a2"
dic = {"a":1, "b":2, "c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
x, y = dic[pos[0]], int(pos[1])

dx = [-2, -2, -1, 1, 2, 2, -1, 1] #위, 오른쪽, 아래, 왼쪽 (시계방향으로)
dy = [-1, 1, 2, 2, -1, 1, -2, -2]


for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<nx<9 and 0<ny<9:
        answer += 1

print(answer)











































