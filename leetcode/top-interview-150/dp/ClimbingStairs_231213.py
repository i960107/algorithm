from typing import List


class Solution:
    def climbStairs(self, n: int):
        if n < 3:
            return n
        path = None
        prev_prev = 1
        prev = 2
        for _ in range(3, n + 1):
            path = prev + prev_prev
            prev_prev, prev = prev, path
        return path


s = Solution()
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
