from typing import List


class Solution:
    def climbStairs(self, n: int):
        if n < 3:
            return n

        dp = [None] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n - 1]


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
