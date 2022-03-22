import bisect
from typing import List


def recursive_binary_serach(nums: List[int], target: int) -> int:
    '''재귀 풀이'''

    # 파이썬에는 재귀 호출에 대한 호출 횟수 제한이 있으며 기본 값은 1,000이다
    # 1000번 재귀호출시 2^1000승개의 숫자에 대한 검사가 이뤄짐
    def binary_search(left, right):
        # left = right인 경우 left=right=mid 모든 값에 대한 검사 끝남
        if left <= right:
            # left +right가 자료형 최댓값을 넘어서는 overflow 발생가능
            # mid = (left + right) // 2
            mid = left + (right - left) // 2

            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid
        else:
            return -1

    # 첫, 마지막 인덱스를 대상으로 binary search
    return binary_search(0, len(nums) - 1)


def binary_search_iterative(nums: List[int], target: int) -> int:
    '''반복 풀이'''
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def binary_search_module(nums: List[int], target: int) -> int:
    '''이진 검색 모듈 활용'''
    # 실제 코딩테스트시 가급적 재귀나 반복으로 직접 이진 검색을 풀이하는 편이 나중에 코드 리뷰시 더 좋은 평가 받을 수 있음
    index1 = bisect.bisect_left(nums, target)
    # bisect_right = bisect
    # 이진 탐색시에는 bisect_left 쓰는게 적합!
    index2 = bisect.bisect(nums, target)
    index3 = bisect.bisect_right(nums, target)
    if index1 < len(nums) and nums[index1] == target:
        return index1
    else:
        return -1


# 못 찾을 경우 가장 첫 원소 혹은 가장 마지막 원소+1 반환
# 중복값 있을 경우 중복된 원소의 가장 첫 번째 원소 인덱스 반환
print(binary_search_module([1, 2, 3, 4, 5], 6))  # index1,index2,index3 = 5
print(binary_search_module([1, 2, 3, 4, 5], 0))  # index1,index2,index3 = 0
print(binary_search_module([2, 2, 3, 4, 5], 2))  # index1=0 index2,index3 = 2
print(binary_search_module([1, 2, 2, 4, 5], 2))  # index1=1 index2,index3 = 3
print(binary_search_module([1, 2, 3, 4, 5], 5))  # index1=4 index2,index3 = 5
print(binary_search_module([1, 2, 3, 4, 5], 1))  # index1=0 index2,index3 = 1


def binary_search_index(nums: List[int], target: int) -> int:
    '''이진 검색을 사용하지 않는 index 풀이'''
    # 복잡도 O(N)
    try:
        # target이 존재하지 않을때 에러 발생
        return nums.index(target)
    # 모든 에러 잡고 싶을때 except Exception 가능 but too broad
    except ValueError:
        return -1
