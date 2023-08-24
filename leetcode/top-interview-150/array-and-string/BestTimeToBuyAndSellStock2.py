from typing import List


class Solution(object):
    # def maxProfit(self, prices: List[int]):
    #     dp = [0] * len(prices)
    #     for i in range(1, len(prices)):
    #         dp[i] = dp[i - 1]
    #         if prices[i] > prices[i - 1]:
    #             dp[i] += prices[i] - prices[i - 1]
    #
    #     return dp[-1]

    def maxProfit(self, prices: List[int]):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += (prices[i] - prices[i-1])
        return profit


s = Solution()
s.maxProfit([7, 1, 5, 3, 6, 4])
s.maxProfit([1, 2, 3, 4, 5])
s.maxProfit([7, 6, 4, 3, 1])
