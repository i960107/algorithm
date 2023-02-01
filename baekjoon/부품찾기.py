# import bisect
from typing import List


# from bisect import bisect_left
#
#
# def solution(N: List[int], M: List[int]) -> List[bool]:
#     '''bisect 모듈 사용'''
#     answer = [False] * len(M)
#
#     N.sort()
#
#     for i, x in enumerate(M):
#
#         res = bisect.bisect_left(N, x)
#         print(res)
#         if 0 <= res < len(N) and N[res] == x:
#             answer[i] = True
#
#     return answer
#
#
# def solution2(N: List[int], M: List[int]) -> List[bool]:
#     N.sort()
#
#     answer = []
#
#     for x in M:
#
#         left, right = 0, len(N) - 1
#         found = False
#
#         while left <= right:
#             mid = left + (right - left) // 2
#             if N[mid] < x:
#                 left = mid + 1
#             elif N[mid] > x:
#                 right = mid - 1
#             else:
#                 found = True
#                 break
#         answer.append(found)
#
#     return answer
#
#
# res = solution([8, 3, 7, 9, 2], [5, 7, 9])
# print(res, res == [False, True, True])
#
# res = solution2([8, 3, 7, 9, 2], [5, 7, 9])
# print(res, res == [False, True, True])

def solution(n: int, parts: List[int], m: int, orders: List[int]) -> List[bool]:
    parts.sort()
    answer = []
    for order in orders:
        if binary_search(order, parts) == -1:
            answer.append("no")
        else:
            answer.append("yes")
    return answer


def binary_search(target: int, numbers: List[int]) -> int:
    lo, hi = 0, len(numbers)
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


print(*solution(5, [8, 3, 7, 9, 2], 3, [5, 7, 9]))
