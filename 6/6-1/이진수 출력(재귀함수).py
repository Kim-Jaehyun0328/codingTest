import sys
sys.stdin=open("in1.txt", "r")

n = int(input())
res = ""
def binary(n):
    global res
    if n == 0 :
        return
    else:
        binary(n // 2)
        res += str(n%2)
        # if n%2 == 0:
        #     res += "0"
        # elif n%2 == 1:
        #     res += "1"

binary(n)
print(res)