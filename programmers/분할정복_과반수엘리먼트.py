from __future__ import annotations

from typing import List
from collections import defaultdict


def solution_dynamic_programming(nums: List[int]) -> int:
    '''메모이제이션을 활용한 풀이'''
    answer = 0
    # 한번에 다 count하는게 아니라 숫자 나올때마다 count... O(n^2)아닌가?

    counts = defaultdict(int)
    # 과반수를 차지하는 -> 절반을 초과하는
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)
            if counts[num] > len(nums) // 2:
                return num

    return answer


def solution_divide_and_conquer(nums: List[int]) -> int | None:
    '''분할 정복을 활용한 우아한~ 풀이'''

    if not nums:
        return None

    if len(nums) == 1:
        return nums[0]

    # mid를 매번 계산하지 않고 mid에 담아두는 것으로 10% 가량 속도를 높일 수 잇다
    mid = len(nums) // 2

    m1 = solution_divide_and_conquer(nums[:mid])
    m2 = solution_dynamic_programming(nums[mid:])

    return [m2, m1][nums.count(m1) > mid]  # m1이 과반수이면 True =1


def solution_pythonic(nums: List[int]) -> int:
    # 정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트?
    return sorted(nums)[len(nums) // 2]


print(solution_dynamic_programming([3, 2, 3]))
print(solution_dynamic_programming([2, 2, 1, 1, 1, 2, 2, ]))
