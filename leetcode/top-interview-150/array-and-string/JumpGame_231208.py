from typing import List


class Solution:
    # 주의 0번째 칸에서 시작도 못할 수도 있음. [0,1]
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i] - 1:
                nums[i + 1] = nums[i] - 1
            if nums[i] == 0:
                return False
        return True

    # 뒤에서부터 첫번째 칸에 도닳할 수 있는지 계산?
    def canJump2(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
