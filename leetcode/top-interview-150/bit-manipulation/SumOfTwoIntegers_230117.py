from typing import List


class Solution:
    def getSum(self, a: int, b: int) -> int:
        def _getSum(c: int, d: int):
            if d == 0:
                return c
            if c == 0:
                return d
            return _getSum(c ^ d, (c & d) << 1)

        return _getSum(a, b)


s = Solution()
print(s.getSum(1, 2))
print(s.getSum(2, 3))
# memory limit exceed
print(s.getSum(1, -1))
