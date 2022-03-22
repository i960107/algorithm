from __future__ import annotations

import bisect
from typing import List


def two_sum_two_pointer(numbers: List[int], target: int) -> List[int] | None:
    '''두 숫자를 더해서 target를 만들수 있는 두 숫자 인덱스를 리턴.중복 원소 없음(정답 한 쌍만 존재).투 포인터 풀'''
    # [i,j] [j,i]는 같지만 두번 검색하게 됨
    # i = j = 0
    # while i < len(numbers) and j < len(numbers):
    #     if numbers[i] >= target:
    #         break
    #     if numbers[i] + numbers[j] < target:
    #         if j != len(numbers) - 1:
    #             j += 1
    #         else:
    #             i += 1
    #             j = 0
    #     elif numbers[i] + numbers[j] > target:
    #         i += 1
    #         j = 0
    #     else:
    #         return [i + 1, j + 1]

    # O(n)
    left, right = 0, len(numbers) - 1
    # left== right면 ? return None
    while not left == right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return [left + 1, right + 1]


def two_sum_binary_search(numbers: List[int], target: int) -> List[int] | None:
    '''이진 검색 풀이'''
    # O(NlogN)
    for i, num in enumerate(numbers):
        required = target - num
        # num 뒤로만 탐색!
        left, right = i + 1, len(numbers) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] < required:
                left = mid
            elif numbers[mid] > required:
                right = mid
            else:
                return [i + 1, mid + 1]


def two_sum_bisec(numbers: List[int], target: int) -> List[int] | None:
    '''bisec모듈 +  슬라이싱 풀이'''
    # O(NlogN)이지만 속도 리스트슬라이싱이 많아 느림
    # slicing 매번 하기 보다 잘라두고 재사용하여 성능 개선시킬 수 있음
    for i, num in enumerate(numbers):
        required = target - num
        # i == len(numbers)-1일때 None반환X []반환
        sliced = numbers[i + 1:]
        j = bisect.bisect_left(sliced, required)
        if len(sliced) > 0 and j < len(sliced) and numbers[i + 1 + j] == required:
            return [i + 1, j + 2 + j]


def two_sum_bisec_without_slicing(numbers: List[int], target: int) -> List[int] | None:
    '''bisec모듈 +  슬라이싱 제거 풀이'''
    for i, num in enumerate(numbers):
        required = target - num
        # left제한하는 parameter 지정
        j = bisect.bisect_left(numbers, required, i + 1)
        if j < len(numbers) and numbers[i] == required:
            return [i + 1, j + 1]


print(two_sum_bisec([2, 7, 11, 15], 15))
print(two_sum_two_pointer([2, 7, 11, 15], 10))
