from __future__ import annotations

import math
from typing import List


def get_max(nums: List[int]) -> int:
    '''분할정복을 사용한 풀이'''
    # 선형 검색과 똑같이 O(N)

    # len(nums) < 1이되는 경우는 없나? 없음!
    # 짝수일때 양쪽 같은 개수로 나눠짐. 홀수일때 뒤가 더 길게
    # 재귀를 멈추는 주건@! 더이상 재귀를 호출하는 코드로 내려가지 않음!
    if len(nums) == 1:
        return nums[0]

    # mid = len(nums) -1 // 2  recursion error 발생
    # 2개 있을때를 기준으로 1개 1개 나눠지려면 앞에 len(nums)//2개 -> slice end index 에들어가면 Index로 자동 변환됨
    # 쪼갰을때 빈 배열이 안됨 최소 원소 개수 1개.
    mid = len(nums) // 2

    # 반환값 int
    left_max = get_max(nums[:mid])
    right_max = get_max(nums[mid:])

    return max(left_max, right_max)


# print(get_max(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(get_max(nums=[1]))
# print(get_max(nums=[5, 4, -1, 7, 8]))


def solution_test(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    mid = len(nums) // 2
    left = solution_test(nums[:mid])
    curr = nums[mid]
    right = solution_test(nums[mid + 1:])
    print(f'nums{nums} left {left} right {right} combined {left + right + curr}')
    return max(left, left + curr + right, right)


# print(solution_test(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(solution_test(nums=[1]))
# print(solution_test(nums=[5, 4, -1, 7, 8]))


def maxSubArray(nums: List[int]) -> int:
    '''divide and conquer'''

    # O(NlogN)
    def findMaxSubArray(nums, left, right):
        # base case - empty array
        if left > right:
            return -math.inf
        mid = left + (right - left) // 2
        curr = best_left_sum = best_right_sum = 0

        for i in range(mid - 1, left - 1, -1):
            curr += nums[i]
            best_left_sum = max(best_left_sum, curr)
        curr = 0
        for i in range(mid + 1, right + 1):
            curr += nums[i]
            best_right_sum = max(best_right_sum, curr)
        best_combined_sum = nums[mid] + best_left_sum + best_right_sum

        left_half = findMaxSubArray(nums, left, mid - 1)
        right_half = findMaxSubArray(nums, mid + 1, right)
        return max(best_combined_sum, left_half, right_half)

    return findMaxSubArray(nums, 0, len(nums) - 1)


# print(maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(maxSubArray(nums=[1]))
# print(maxSubArray(nums=[5, 4, -1, 7, 8]))


def maxSubArrayDynamic(nums: List[int]) -> int:
    '''dynamic programming '''
    # O(N)
    # 0으로 초기화하면 안됨! dp[0] = nums[0]과 같아야 함!
    # 각 원소까지의 원소들로 만들수 있는 subarray들 중 최대 값.
    # 어떤 subarray든 현재 원소 포함하고 있으므로 연속적인 subarray가 됨.
    dp = [num for num in nums]
    for i in range(1, len(nums)):
        # 현재 위치까지 subarray들의 합중 최고인 것을 현재 원소로 대체!
        # cur_sub 필요 없음! dp 배열 꼭 필요한가? nums에 덮어쓰면?
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    # 엥 ? max[dp]?
    # nums[-1] 아님 중간에 멈추는게 더나았을수있음! 분명!
    return max(dp)


def maxSubArrayDynamic2(nums: List[int]) -> int:
    '''dynamic programming - Kadene's Algorithm'''

    # initialize our variable using the first element
    # cur_sub는 현재 원소까지 연결한 subarray의 합
    # 따로 배열에 각 원소까지의 max값 저장해두고 max()로 계산하면 O(N) 복잡도 추가됨. max변수로 매번 비교해주는게 더 빠름
    cur_sub = max_sub = nums[0]

    # start with the 2nd element since we already used the first one
    for i in range(1, len(nums)):
        # 현재까지 다 더한 sub array?
        # if current subarray is negative, throw it away. otherwise, keep adding to it
        # 연속적이거나 현재 원소부터 시작하거나!
        cur_sub = max(nums[i], cur_sub + nums[i])
        max_sub = max(max_sub, cur_sub)

    return max_sub


def maxSubArrayDynamic3(nums: List[int]) -> int:
    local = glob = 0
    for n in nums:
        # local은 현재까지 중 max_sub_array
        local = max(n, local + n)
        glob = max(glob, local)
    return glob


print(maxSubArrayDynamic(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArrayDynamic(nums=[1]))
print(maxSubArrayDynamic(nums=[5, 4, -1, 7, 8]))

print(maxSubArrayDynamic3(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArrayDynamic3(nums=[1]))
print(maxSubArrayDynamic3(nums=[5, 4, -1, 7, 8]))
