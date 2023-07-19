import sys
sys.stdin=open("in5.txt", "r")

list_ = [(i+1) for i in range(20)]

for i in range(10):
    start, end = map(int, input().split())
    temp = 0
    for j in range((end-start+1)//2):
        temp = list_[start-1+j]
        list_[start-1+j] = list_[end-1-j]
        list_[end-1-j] = temp

print(list_)