from collections import deque


def solution(cacheSize, cities):
    cache = deque([])
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()
    return answer


result = solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
print(result)