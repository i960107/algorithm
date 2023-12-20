from typing import List


class Solution:
    # peak이 여러개일 경우 랜덤하게 하나 반환.
    # O(LogN)알고리즘 이어야함 -> binary search . 그 외에 뭐가 있을가?
    def findPeakElement(self, nums: List[int]):
        lo, hi = 0, len(nums) - 1
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            # 오르막 혹은 peak
            if mid - 1 < 0 or nums[mid] > nums[mid - 1]:
                res = mid
                lo = mid + 1
            elif nums[mid] < nums[mid - 1]:
                hi = mid - 1
            # 내리막 혹은 저점
        return res


s = Solution()
print(s.findPeakElement([-4]))
print(s.findPeakElement([1, 2, 3, 1]))
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
