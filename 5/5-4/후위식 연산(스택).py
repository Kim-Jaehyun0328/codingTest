import sys
sys.stdin=open("in5.txt", "r")

s = input()
stack = []
for x in s:
    if x.isdecimal():
        stack.append(int(x))
    else:
        num2, num1 = stack.pop(), stack.pop()
        if x == "+":
            temp = num1 + num2
        elif x == "-":
            temp = num1 - num2
        elif x == "*":
            temp = num1 * num2
        elif x == "/":
            temp = num1 / num2
        stack.append(temp)


print(stack.pop())