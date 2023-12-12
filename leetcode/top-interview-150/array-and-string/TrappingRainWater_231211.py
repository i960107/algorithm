from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right - 1:
            # 먼저 max 를 조정해주어야함. 아니면 left_max < height[left]여서 water 가 음수인 경우에도 더해짐.
            # 인덱스 이동 시기, max조정시기, water더해주는 시기
            if left_max <= right_max:
                left += 1
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += (left_max - height[left])
            else:
                right -= 1
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += (right_max - height[right])
        return water


s = Solution()
# print(s.trap([4, 2, 0, 3, 2, 5]))
# print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]))
