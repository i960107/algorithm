from typing import List


class Solution:
    def candy(self, nums: List[int]):
        ans = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                ans[i] = ans[i - 1] + 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1] and ans[i] <= ans[i + 1]:
                # 이미 크다 -> ans[i] > ans[i + 1] 갱신하면 왼쪽 이웃보다 적은 수를 가지게 됨.
                ans[i] = ans[i + 1] + 1
        return ans

    def candy2(self, nums: List[int]):
        # 누적합 양쪽으로 고려하여 둘 중 큰 값.
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                right[i] = right[i + 1] + 1
        total = 0
        for i in range(len(nums)):
            if left[i] > right[i]:
                total += left[i]
            else:
                total += right[i]
        return total


s = Solution()
print(s.candy([1, 2, 1]))
print(s.candy([1, 2, 2]))
print(s.candy([1, 0, 2]))
print(s.candy([1, 2, 0, 3, 4, 2, 3]))
print(s.candy2([1, 2, 1]))
print(s.candy2([1, 2, 2]))
print(s.candy2([1, 0, 2]))
print(s.candy2([1, 2, 0, 3, 4, 2, 3]))
