import sys
sys.stdin=open("in1.txt", "r")

a = input()
res = ""
stack = []
for i in range(len(a)):
    if a[i].isdigit():
        res += a[i]
    else:
        if not stack:
            stack.append(a[i])
        elif (stack[-1] == "+" or stack[-1] == "-") and (a[i] == "*" or a[i] == "/"):
            stack.append(a[i])
        elif (stack[-1] == "*" or stack[-1] == "/") and (a[i] == "+" or a[i] == "-"):
            while True:
                if len(stack) == 0 or stack[-1] == "(":
                    break
                res += stack.pop()
            stack.append(a[i])
        elif (stack[-1] == "+" or stack[-1] == "-") and (a[i] == "+" or a[i] == "-"):
            res += stack.pop()
            stack.append(a[i])
        elif (stack[-1] == "*" or stack[-1] == "/") and (a[i] == "*" or a[i] == "/"):
            res += stack.pop()
            stack.append(a[i])
        elif a[i] == "(":
            stack.append(a[i])
        elif a[i] == ")":
            while True:
                if stack[-1] == "(":
                    stack.pop()
                    break
                else:
                    res += stack.pop()
        else:
            stack.append(a[i])

while stack:
    res += stack.pop()

print(res)