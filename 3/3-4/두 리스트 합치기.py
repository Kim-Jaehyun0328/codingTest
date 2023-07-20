import sys
sys.stdin=open("in1.txt", "r")

N = int(input())
list1 = list(map(int, input().split()))
M = int(input())
list2 = list(map(int, input().split()))
res = []
point1, point2 = 0,0

while True:
    if len(res) == N+M:
        break
    elif len(list1) == point1:
        res = res + list2[point2:]
        # for i in range(point2, len(list2)):
        #     res.append(list2[i])
        break
    elif len(list2) == point2:
        res = res + list1[point1:]
        # for j in range(point1, len(list1)):
        #     res.append(list1[j])
        break
    if list1[point1] <= list2[point2] :
        res.append(list1[point1])
        point1 += 1
    else:
        res.append(list2[point2])
        point2 += 1

for i in range(len(res)):
    print(res[i], end=" ")