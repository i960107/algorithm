from __future__ import annotations

from typing import List, Optional
from collections import defaultdict
from collections import Counter


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
    # 재귀 풀이의 특성상 다이나믹 프로그래밍에 비해 느림

    # O(NLogN)
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
    # 반드시 과반수 이상을 차지하는 엘리먼트가 있을때 사용 가능
    # 정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트?
    # len(nums)//2 +1 번째 원소를 찾아야함. index 상 len(nums)//2
    return sorted(nums)[len(nums) // 2]


def solution_test(nums: List[int]) -> Optional[int]:
    # 짝수면 안돼. 홀수로 쪼개야해
    # 빈 배열이거나 원소의 개수가 1이면
    if not nums:
        return None

    # 한개가 될때까지 쪼개
    if len(nums) == 1:
        return nums[0]

    # 사실 조합하는 부분이 와따지
    # 원소의 개수가 2개이상이면
    # len(m2)>=len(m1)
    mid = len(nums) // 2
    m1 = solution_test(nums[:mid])
    m2 = solution_test(nums[mid:])

    # O(N^2)이 되지 않나?
    # 과반수 후보군에 해당하는 엘리먼트만 리턴
    # m1이 리스트에서 과반수를 차지한다면 [m2,m1][1]로 m1반환
    # len(nums) == 2일때 다른 숫자라면 False이르모 m2반환 둘중 어떤걸 반환해도 됨?
    # 같은 비율로 있다면 m1반환?
    # m1이 과반수 이상일때만 m1반환. 같은 비율이라면 m2반환
    return [m2, m1][nums.count(m1) > mid]


print(solution_dynamic_programming([3, 2, 3]))
print(solution_test([3, 2, 3]))
print(solution_dynamic_programming([2, 2, 1, 1, 1, 2, 2, ]))
print(solution_test([2, 2, 1, 1, 1, 2, 2, ]))
print(solution_dynamic_programming([2, 2, 1, 1, 1, 2, 2, ]))
print(solution_test([2, 2, 1, 1, 1, 2, 2, ]))
