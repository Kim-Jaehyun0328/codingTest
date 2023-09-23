elements = [7, 9, 1, 1, 4]

temp = []

for i in range(1, len(elements) + 1):
    for j in range(len(elements)):
        if i + j > len(elements):
            temp.append(sum(elements[j:i + j]) + sum(elements[0:i + j - len(elements)]))
        else:
            temp.append(sum(elements[j:i + j]))

temp = list(set(temp))

print(len(temp))