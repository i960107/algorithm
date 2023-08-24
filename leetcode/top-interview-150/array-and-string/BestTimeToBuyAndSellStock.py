from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit = prices[i] - prices[i - 1]
                if max_profit < profit:
                    max_profit = profit
                prices[i] = prices[i - 1]

        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        stack = []
        max_profit = 0
        for p in prices:
            if not stack or stack[-1] > p:
                stack.append(p)
            else:
                profit = p - stack[-1]
                if max_profit < profit:
                    max_profit = profit
        return max_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
