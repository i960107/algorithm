from typing import List


class Solution:
    def mySqrt(self, s: int) -> int:
        lo, hi = 0, s
        ans = 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= s:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans


s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))
print(s.mySqrt(16))
print(s.mySqrt(122))
