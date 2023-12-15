from typing import List


class Solution:
    # 정렬된 배열에서 target보다 크거나 같은 값 중 가장 왼쪽 값.
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        pos = len(nums)
        # 주의 등호 포함되어야함. 모든 원소가 검사되어야함.
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                pos = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return pos


s = Solution()
# print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 0))
# print(s.searchInsert([1, 3, 5, 6], 7))
#
print(s.searchInsert([1, 3, 5, 6], 2))
