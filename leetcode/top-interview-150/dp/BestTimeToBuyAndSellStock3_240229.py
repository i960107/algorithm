from math import inf
from typing import List


class Solution:
    # 최대 두번까지 거래 가능.
    # O(N^2)을 구해서 두개를 더한다.
    # 1. dp(memoization, recursion)
    # 2. divide and conquer.

    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = [inf] * 2, [0] * 2
        for x in prices:
            for i in range(2):
                if i:
                    buy[i] = min(buy[i], x - sell[i - 1])
                else:
                    buy[i] = min(buy[i], x)
                sell[i] = max(sell[i], x - buy[i])
        return sell[1]

    # divide and conquer -> efficiently
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        # 최대값이 최소값의 오른쪽에 있는 것을 어떻게 보장함?
        max_price, min_price = [prices[0]] * n, [prices[0]] * n
        max_price_reverse, min_price_reverse = [prices[n - 1]] * n, [prices[n - 1]] * n
        profit, min_stock = [0] * n, prices[0]
        profit_reverse, max_stock = [0] * n, prices[n - 1]

        for i in range(1, n):
            max_price[i] = max(max_price[i - 1], prices[i])
            min_price[i] = min(min_price[i - 1], prices[i])
            profit[i] = max(profit[i - 1], prices[i] - min_stock)
            if min_stock > prices[i]:
                min_stock = prices[i]

        for i in range(n - 2, -1, -1):
            max_price_reverse[i] = max(max_price_reverse[i + 1], prices[i])
            min_price_reverse[i] = min(min_price_reverse[i + 1], prices[i])
            profit_reverse[i] = max(profit_reverse[i + 1], max_stock - prices[i])
            if max_stock < prices[i]:
                max_stock = prices[i]

        print(profit)
        print(profit_reverse)

        max_profit = profit_reverse[0]
        for i in range(1, n):
            max_profit = max(max_profit,
                             profit[i - 1] + profit_reverse[i])
        return max_profit


s = Solution()
print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(s.maxProfit2([3, 3, 5, 0, 0, 3, 1, 4]))
print(s.maxProfit2([1, 2, 3, 4, 5]))
