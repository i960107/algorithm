import bisect
from typing import List


def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    '''두 배열간 최소거리 찾기'''
    count = 0
    arr2.sort()
    for x in arr1:
        l, u = 0, len(arr2) - 1
        while l <= u:
            mid = l + (u - l) // 2
            if arr2[mid] - x <= d:
                break
            else:
                pass
        count += 1
    return 0


def findTheDistanceValueModule(arr1: List[int], arr2: List[int], d: int) -> int:
    # O(NlogN)
    answer = 0
    arr2.sort()
    for x in arr1:
        i = bisect.bisect_left(arr2, x)
        # 가장 가까운 원소!
        if i == 0:
            if arr2[i] - x > d:
                answer += 1
        elif i == len(arr2):
            if x - arr2[i - 1] > d:
                answer += 1
        elif arr2[i] - x > d and x - arr2[i - 1] > d:
            answer += 1
    return answer


print(findTheDistanceValueModule([4, 5, 8], [10, 9, 1, 8], 2))  # 2
print(findTheDistanceValueModule([4, 5, 8], [4], 2))  # 2
print(findTheDistanceValueModule(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))  # 2
print(findTheDistanceValueModule(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))  # 1
