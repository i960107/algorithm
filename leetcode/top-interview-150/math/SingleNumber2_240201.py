from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0  # 홀수번 등장한 bit들만 1
        twos = 0  # 2번이상 등장한 bit들만 1.
        for num in nums:
            ones = (ones ^ num) & (~twos)  # 홀수번등장했으면서 2번이상 등장하지 않은 애들만.
            twos = (twos ^ num)  # 2번 등장한 애들 중 1번 등장하지 않은 애들만.
        return ones

    def singleNumber2(self, nums: List[int]) -> int:
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes


s = Solution()
# print(s.singleNumber([1, 2, 1, 2, 1]))
# print(s.singleNumber([1, 2, 1, 2, 2]))
print(s.singleNumber([2, 2, 3, 2]))
# print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))
