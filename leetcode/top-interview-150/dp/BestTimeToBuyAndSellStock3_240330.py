from typing import List


class Solution:
    # maximum profit of at most two transactions
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profits = [0] * n
        min_price = prices[0]
        # 단순히 최소값이 아니라 0 ~ i번째날까지 얻을 수 있는 profit의 최대값.
        for i in range(1, n):
            profit = prices[i] - min_price
            if profit > profits[i - 1]:
                profits[i] = profit
            else:
                profits[i] = profits[i - 1]

            if min_price > prices[i]:
                min_price = prices[i]

        profits_reverse = [0] * n
        max_price = prices[n - 1]
        for i in range(n - 2, -1, -1):
            profit = max_price - prices[i]
            if profit < profits_reverse[i + 1]:
                profits_reverse[i] = profits_reverse[i + 1]
            else:
                profits_reverse[i] = profit

            if prices[i] > max_price:
                max_price = prices[i]

        print(profits, profits_reverse)
        # 두 부분으로 나누어서(0 ~ i-1, i ~ n -1)
        # 각 구간의 max profit 의 합 -> total max profit
        max_profit = 0
        for i in range(1, n - 1):
            # 0은 고려하지 않아도 되는 이유.
            # -> 0이나 n-1일 둘 중 하나 고려 필요.
            total_profit = profits[i] + profits_reverse[i]
            # i ~ i+1에서 얻을 수 있는 profit은 제외됨.
            # total_profit = profits[i] + profits_reverse[i + 1]
            if total_profit > max_profit:
                max_profit = total_profit
        return max_profit


s = Solution()
print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
