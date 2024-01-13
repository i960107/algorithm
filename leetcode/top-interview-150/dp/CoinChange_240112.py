from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [INF for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
        return dp[amount] if dp[amount] != INF else - 1


s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([1, 5, 7], 10))
print(s.coinChange([5, 7], 10))
print(s.coinChange([2], 3))
print(s.coinChange([1], 0))
