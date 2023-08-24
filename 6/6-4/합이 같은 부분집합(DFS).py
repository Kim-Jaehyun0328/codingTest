# import sys
# sys.stdin=open("in4.txt", "r")
#
#
# n = int(input())
# num_list = list(map(int, input().split()))
# flag = False
#
# def DFS(v):
#     global num_list
#     global flag
#     if v == n :
#         b = set(num_list) - set(a)
#         if sum(a) == sum(b):
#             flag = True
#         return
#     else:
#         a.append(num_list[v])
#         DFS(v+1)
#         a.pop()
#         DFS(v+1)
#
# a= []
# DFS(0)
# if flag:
#     print("YES")
# else:
#     print("NO")



import sys
sys.stdin=open("in1.txt", "r")


n = int(input())
num_list = list(map(int, input().split()))

def DFS(v, sum):
    if sum > total//2:
        return
    if v == n:
        if sum == (total - sum):
            print("YES")
            sys.exit()
    else:
        DFS(v+1, sum + num_list[v])
        DFS(v+1, sum)

total = sum(num_list)
DFS(0, 0)
print("NO")
