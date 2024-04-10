from typing import List


class Solution:
    # max two transactions
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        max_transactions = 2
        HOLDING = 0
        NONE = 1

        dp = [[float('-INF'), float('-INF')] for _ in range(max_transactions)]
        dp[0] = [-prices[0], 0]
        for i in range(1, n):
            price = prices[i]
            for numTransactions in range(max_transactions):
                dp[numTransactions][HOLDING] = max(dp[numTransactions - 1][NONE] if numTransactions != 0 else 0 - price,
                                                   # 새로 사거나
                                                   dp[numTransactions - 1][HOLDING])  # 가지고 있거나
                dp[numTransactions][NONE] = max(dp[numTransactions - 1][NONE],  # 그대로거나
                                                dp[numTransactions - 1][HOLDING] + price)  # 팔거나
                print(f"%d번째 날까지 거래가 최대 %d번 일어났을때 이익 : %f, %f" % (
                    i + 1, numTransactions , dp[numTransactions][HOLDING], dp[numTransactions][NONE]))
        return dp[max_transactions - 1][1]


s = Solution()
# print(s.maxProfit([3]))
print(s.maxProfit([3, 4]))
# print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
# print(s.maxProfit([1, 2, 3, 4, 5]))
# print(s.maxProfit([7, 6, 4, 3, 1]))
