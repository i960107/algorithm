from typing import List
import heapq


def solution(cards: List[List[int]]) -> int:
    max_h = []

    for row in cards:
        min_of_row = min(row)
        heapq.heappush(max_h, -min_of_row)

    return -heapq.heappop(max_h)


res = solution([[3, 1, 2], [4, 1, 4], [2, 2, 2]])
print(res == 2)
