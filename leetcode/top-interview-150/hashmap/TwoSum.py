from typing import List
from collections import defaultdict


# 서로 다른 두 원소
# 중복된 원소 사용할 수 없음

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)

        for i, n in enumerate(nums):
            if target - n != n and target - n in d:
                return [i, d[target - n][0]]
            elif target - n == n and len(d[n]) == 2:
                return d[n]

    # 최대 한번만 배열을 순회하면서 해결 가능.
    # 중복된 원소가 있는 경우에도  n + n == target인 경우 이미 있는 인덱스와 쌍으로 반환
    #  n + n != target인데 n + m == target인 경우는 없음. 정확히 한 쌍의 해만 존재한다고 했으므로. 인덱스 덮어써도 됨.
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, n in enumerate(nums):
            if target - n in d:
                return [i, d[target - n]]
            d[n] = i
    # 투포인터 접근법
    # def twoSum2(self, nums: List[int], target: int) -> List[int]:
    #     i = 0
    #     j = len(nums) - 1
    #     while i < j:
    #         # 배열에 규칙이 있는 것이 아니기 때문에 어떤 포인터를 옮길것인지 결정하기 어려움.
    #         if nums[i] + nums[j] == target:
    #             return [i, j]


s = Solution()
print(s.twoSum2([2, 7, 11, 15], 9))
print(s.twoSum2([3, 2, 4], 6))
print(s.twoSum2([3, 3, 4, 1], 6))
