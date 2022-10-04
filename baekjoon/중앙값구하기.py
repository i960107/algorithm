import heapq
from typing import List


def solution(N: int, arr: List[int]) -> List[int]:
    min_h, max_h = [], []
    answer = []
    for i, num in enumerate(arr):
        if i == 0 or min_h[0] < num:
            heapq.heappush(min_h, num)
        else:
            heapq.heappush(max_h, -num)

        if not i & 1:
            while i and len(max_h) < i // 2:
                heapq.heappush(max_h, -heapq.heappop(min_h))
            while i and len(min_h) < i // 2 + 1:
                heapq.heappush(min_h, -heapq.heappop(max_h))
            answer.append(min_h[0])
    return answer


def solution2(N: int, arr: List[int]) -> List[int]:
    max_h, min_h = [], []

    def put(num: int):
        if max_h and -max_h[0] <= num:
            heapq.heappush(min_h, num)
        else:
            heapq.heappush(max_h, -num)

        # |min_h| <= |max_h| <= |min_h| + 2
        if len(max_h) > len(min_h) + 2:
            heapq.heappush(min_h, -heapq.heappop(max_h))
        elif len(max_h) < len(min_h):
            heapq.heappush(max_h, -heapq.heappop(min_h))

    answer = []
    for i, val in enumerate(arr):
        put(val)
        if not i & 1:
            print(max_h)
            print(min_h)
            answer.append(-max_h[0])

    return answer

    pass


# print(solution(9, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution2(9, [9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(solution2(23,
                [23, 41, 13, 22, -3, 24, -31, -11, -8, -7, 3, 5, 100, 211, -311, -45, -67, -73, -81, -99, -33, 24, 56]))
