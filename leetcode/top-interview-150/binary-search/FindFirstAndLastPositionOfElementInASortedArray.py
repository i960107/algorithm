import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1

        start = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                start = mid
                hi = mid - 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        end = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    end = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return [start, end]


s = Solution()
print(s.searchRange2([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange2([5, 7, 7, 10], 8))
print(s.searchRange2([], 8))
