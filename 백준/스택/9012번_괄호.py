import sys
N = int(sys.stdin.readline())

for _ in range(N):
    stack = []
    vps = sys.stdin.readline().strip()
    for i in vps:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")