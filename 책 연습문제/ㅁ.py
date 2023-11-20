n = 20

prime = [0 for _ in range(n+1)]
answer = 0
for i in range(2, len(prime)):
    if prime[i] != 0:
        continue
    else:
        answer += 1
        print(i)
        for j in range(i, len(prime), i):
            prime[j] += 1

print(answer)

