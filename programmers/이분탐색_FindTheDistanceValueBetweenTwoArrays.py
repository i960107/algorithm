import bisect
from typing import List


def findDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    '''이진검색 - iterative version'''
    # arr1 각각의 원소에 대해서 arr2에서 가장 가까운 원소와 그 거리 찾기
    # O(NlogN)
    arr2.sort()

    def findNearestValue(a: int) -> int:
        # bisect left와 같나?
        '''arr2에서 a와 가장 가까운 원소 찾기'''
        l, u = 0, len(arr2) - 1
        # O(logN)
        while l <= u:
            mid = l + (u - l) // 2
            if arr2[mid] == a:
                return arr2[mid]
            elif arr2[mid] < a:
                l = mid + 1
            else:
                u = mid - 1
        # 찾지 못하고 빠져나올 경우 l > u
        #  u index out or range될 수 있음! l도?
        # index = bisect.bisect_left(arr2, a)
        # if index == 0:
        #     return arr2[index]
        # elif index == len(arr2):
        #     return arr2[-1]
        # else:
        #     if abs(arr2[index] - a) < abs(arr2[index - 1] - a):
        #         return arr2[index]
        #     else:
        #         return arr2[index - 1]
        # 잘못된 버전
        # return arr2[index] if index < len(arr2) and abs(arr2[index] - a) < abs(arr2[index - 1] - a) else arr2[-1]
        return arr2[l] if l < len(arr2) and abs(arr2[l] - a) < abs(arr2[u] - a) else arr2[u]

    count = 0

    # (ONlogN)
    for a in arr1:
        # 가장 가까운 거리의 value
        dist = abs(a - findNearestValue(a))
        if dist > d:
            count += 1

    return count


def findDistanceValue_biesct(arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()

    def findNearestValue(a: int) -> int:
        '''arr2에서 a와 가장 가까운 원소 찾기'''
        index = bisect.bisect_left(arr2, a)
        if index == 0:
            return arr2[index]
        elif index == len(arr2):
            return arr2[-1]
        else:
            if abs(arr2[index] - a) < abs(arr2[index - 1] - a):
                return arr2[index]
            else:
                return arr2[index - 1]
        # 잘못된 버전
        # return arr2[index] if index < len(arr2) and abs(arr2[index] - a) < abs(arr2[index - 1] - a) else arr2[-1]

    count = 0

    # (ONlogN)
    for a in arr1:
        # 가장 가까운 거리의 value
        dist = abs(a - findNearestValue(a))
        if dist > d:
            count += 1

    return count


# 투포인터로 풀 수 있을까?
print(findDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
print(findDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20], 3))
print(findDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))
print(findDistanceValue([4, 5, 8], [1], 2))
# 0이되는 게 맞음! 1과 가장 가까운 원소는 1 <= 2
print(findDistanceValue([1], [10, 9, 1, 8], 2))
print(findDistanceValue(
    [-803, 715, -224, 909, 121, -296, 872, 807, 715, 407, 94, -8, 572, 90, -520, -867, 485, -918, -827, -728, -653,
     -659, 865, 102, -564, -452, 554, -320, 229, 36, 722, -478, -247, -307, -304, -767, -404, -519, 776, 933, 236, 596,
     954, 464]
    , [817, 1, -723, 187, 128, 577, -787, -344, -920, -168, -851, -222, 773, 614, -699, 696, -744, -302, -766, 259, 203,
       601, 896, -226, -844, 168, 126, -542, 159, -833, 950, -454, -253, 824, -395, 155, 94, 894, -766, -63, 836, -433,
       -780, 611, -907, 695, -395, -975, 256, 373, -971, -813, -154, -765, 691, 812, 617, -919, -616, -510, 608, 201,
       -138, -669, -764, -77, -658, 394, -506, -675, 523, 730, -790, -109, 865, 975, -226, 651, 987, 111, 862, 675,
       -398, 126, -482, 457, -24, -356, -795, -575, 335, -350, -919, -945, -979, 611]
    , 37))
