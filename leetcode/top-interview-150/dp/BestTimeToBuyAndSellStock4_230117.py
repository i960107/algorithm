from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for cap in range(1, k + 1):
                # dp[i][0][cap] : buying
                dp[i][0][cap] = max(dp[i + 1][0][cap], -prices[i] + dp[i + 1][1][cap])
                # dp[i][1][cap] : selling
                dp[i][1][cap] = max(dp[i + 1][1][cap], prices[i] + dp[i + 1][0][cap - 1])
        # 0번째 날에 샀을때 0 ~ n까지 최대 profit k번 거래.
        return dp[0][0][k]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n)]
        if n <= 1 or k == 0: return 0
        # k >= n. best time to buy and sell stock2와 같음.
        # 1 <= k < n
        dp[0][0][0] = -prices[0]
        for i in range(1, n):
            for cap in range(1, k + 1):
                # 0 bought. 1: not holding any stock.
                # dp[i][0][cap] : buying. must sell yesterday.
                # holding already bought stock, buying new stock.
                dp[i][0][cap] = max(dp[i - 1][0][cap], -prices[i] + dp[i - 1][1][cap])
                # dp[i][1][cap] : selling
                # remain no state or selling holding stock
                dp[i][1][cap] = max(dp[i - 1][1][cap], prices[i] + dp[i - 1][0][cap - 1])
        # 0번째 날에 샀을때 0 ~ n까지 최대 profit k번 거래.
        print(dp)
        return max(dp[n - 1][1][k], dp[n - 1][0][k])


s = Solution()
print(s.maxProfit(2, [2, 4, 1]))
