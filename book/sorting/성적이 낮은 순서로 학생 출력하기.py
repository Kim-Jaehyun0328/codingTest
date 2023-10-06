N = 2
l = [["홍길동", 95], ["이순신", 77]]

l.sort(key=lambda x:x[1])

for x in l:
    print(x[0], end=" ")