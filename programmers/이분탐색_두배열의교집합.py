import bisect
from typing import List
from typing import Set


def intersection_of_two_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    '''두배열의 교집합(중복제거) - 이진 검색 '''
    nums1 = sorted(list(set(nums1)))
    nums2 = sorted(list(set(nums2)))
    answer = []

    for i in range(min(len(nums1), len(nums2))):
        target = nums1[i] if len(nums1) <= len(nums2) else nums2[i]
        left, right = 0, max(len(nums1), len(nums2)) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = nums2[mid] if len(nums1) <= len(nums2) else nums1[mid]
            if mid_value < target:
                left = mid + 1
            elif mid_value > target:
                right = mid - 1
            else:
                answer.append(mid_value)
                break

    return answer


print(intersection_of_two_arrays([1, 2, 2, 1], [2, 2]))
print(intersection_of_two_arrays([4, 9, 5], [9, 4, 9, 8, 4]))


def intersection_bisec(nums1: List[int], nums2: List[int]) -> List[int]:
    '''이진 검색 모듈 활용 풀이'''
    result: Set = set()
    # 정렬된 상태에서 이진 탐색
    # O(NlogN)
    nums2.sort()

    # 이진 검색 자체가 효율적인 검색 알고리즘이므로 탐색하는 숫자 상관없음? 짤은 배열의 원소를 대상으로 검사하는게 낫지 않나?
    # 순서대로 탐색
    for n1 in nums1:
        # 이진 검색
        i2 = bisect.bisect_left(nums2, n1)
        # 예외처리
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)
    return list(result)


def intersection_brute_force(nums1: List[int], nums2: List[int]) -> List[int]:
    '''브루트 포스 풀이 : 선형검색. 가능한 모든 해를 검사'''
    # O(N^2)복잡
    # 검사하는 배열자체를 set으로 만들기 vs result를 set으로 만들기
    result: Set = set()
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)
    return list(result)


def intersection_two_pointer(nums1: List[int], nums2: List[int]) -> List[int]:
    '''양쪽다 정렬후 투포인터 비교'''
    # 병합정렬시 마지막에 최종 결과를 비교하는 과정과 유사?
    # O(NlogN)
    result: Set = set()
    # 양쪽 모두 정렬
    nums1.sort()
    nums2.sort()
    # i는 nums1을 가리키고, j는 nums2를 가리킨다

    i = j = 0
    while i < len(nums1) and j > len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1

    return list(result)
