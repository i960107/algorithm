from typing import List
from bisect import bisect_left


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2 = set(nums2)
        ans = []
        for n in nums2:
            pos = bisect_left(nums1, n, 0, len(nums1))
            if pos < len(nums1) and nums1[pos] == n:
                ans.append(n)
        return ans


s = Solution()
print(s.intersection([1, 2, 2, 1], [2, 2]))
