from typing import List
from collections import deque


def solution(cache_size: int, cities: List[str]) -> int:
    cache = deque()

    for city in cities:
        cache_hit = False
        for _ in range(cache_size):
            curr = cache.popleft()
            if curr == city:
                cache_hit = True
                




print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
