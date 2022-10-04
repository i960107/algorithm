import bisect
from typing import List
from bisect import bisect_left


def solution(N: List[int], M: List[int]) -> List[bool]:
    '''bisect 모듈 사용'''
    answer = [False] * len(M)

    N.sort()

    for i, x in enumerate(M):

        res = bisect.bisect_left(N, x)
        print(res)
        if 0 <= res < len(N) and N[res] == x:
            answer[i] = True

    return answer


def solution2(N: List[int], M: List[int]) -> List[bool]:
    N.sort()

    answer = []

    for x in M:

        left, right = 0, len(N) - 1
        found = False

        while left <= right:
            mid = left + (right - left) // 2
            if N[mid] < x:
                left = mid + 1
            elif N[mid] > x:
                right = mid - 1
            else:
                found = True
                break
        answer.append(found)

    return answer


res = solution([8, 3, 7, 9, 2], [5, 7, 9])
print(res, res == [False, True, True])

res = solution2([8, 3, 7, 9, 2], [5, 7, 9])
print(res, res == [False, True, True])
