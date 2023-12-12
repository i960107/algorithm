from typing import List


class Solution:
    def productExceptSelf2(self, nums: List[int]):
        answer = [1] * len(nums)
        acc = 1
        for i in range(len(nums)):
            answer[i] *= acc
            acc *= nums[i]
        acc = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= acc
            acc *= nums[i]
        return answer

    # 전체 곱을 구하고 그 원소가 제외한다 -> 0이 있는 경우 안됨.
    def productExceptSelf(self, nums: List[int]):
        total_multiple = 1
        for n in nums:
            total_multiple *= n
        for i in range(len(nums)):
            # 0으로 나누는 경우 주의하기!
            nums[i] = (total_multiple // nums[i] if nums[i] != 0 else 0)
        return nums


s = Solution()
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
print(s.productExceptSelf([1, 2, 3, 4]))
