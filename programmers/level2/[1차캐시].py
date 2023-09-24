cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
answer = 0
cache = []

for x in cities:
    x = x.lower()
    if x in cache:
        answer += 1
        cache.remove(x)
        cache.append(x)
    else:
        if len(cache) < cacheSize:
            cache.append(x)
        else:
            cache.append(x)
            cache.pop(0)
        answer += 5

print(answer)

