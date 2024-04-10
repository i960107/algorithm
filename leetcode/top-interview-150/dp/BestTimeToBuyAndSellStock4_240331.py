from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0, 0] for _ in range(k)] for _ in range(n)]
        pass

    def maxProfit2(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if k == 0:

            return 0
        if k > n // 2:
            return sum(prices[i] - prices[i - 1] if prices[i] > prices[i - 1] else 0 for i in range(1, n))

        buyPrice = [0] * (k + 1)  # buyPrice[i] : 거래횟수가 최대 i번이고, 주식을 가지고 있는 상태
        profit = [0] * (k + 1)  # profit[i] : 거래횟수가 최대 i번이고, 주식을 가지고 있지 않은 상태에서 얻을 수 있는 최대 이익

        for day in range(n):
            price = prices[day]
            for i in range(1, k + 1):
                buyPrice[i] = min(buyPrice[i], price - (profit[i - 1] if i != 1 else 0))
                profit[i] = max(profit[i], price - buyPrice[i])
        return int(profit[k])

    def maxProfit3(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if k == 0:
            # 거래 일어날 수 없음
            return 0
        if k > n // 2:
            # 거래 무한정 일어날 수 있음.
            return sum(prices[i] - prices[i - 1] if prices[i] > prices[i - 1] else 0 for i in range(1, n))

        INF = float('-INF')
        dp = [[[INF, INF] for _ in range(k + 1)] for _ in range(n + 1)]
        for day in range(1, n + 1):
            dp[day][0][0] = max(dp[day - 1][0][0], -prices[day - 1])  # 거래가 한번도 안 일어났을때는 그날까지 가장 작은 주식을 보유하는 수밖에.
            dp[day][0][1] = 0

        # 거래가 정확히 한번 일어난걸 어떻게 표시하지. 아래 풀이는 안됨. 0으로 초기화했기 때문에 거래 안하는게 더 나을 경우 0이 선택됨(거래 안하는 경우)
        for noTransactions in range(1, k + 1):
            for day in range(2, n + 1):
                price = prices[day - 1]
                dp[day][noTransactions][0] = max(dp[day - 1][noTransactions][0],  # 가지고 있던걸 계속 가지고 있든가
                                                 dp[day - 1][noTransactions][1] - price)  # 주식을 새로 삼
                dp[day][noTransactions][1] = max(price + dp[day - 1][noTransactions - 1][0],  # 가지고 있던 주식을 팔든가
                                                 dp[day - 1][noTransactions][1])  # 그대로 가든가
        return max(dp[n][noTransactions][1] for noTransactions in range(1, k + 1))


s = Solution()
print(s.maxProfit2(k=2, prices=[3, 2, 6, 5, 0, 3]))
print(s.maxProfit3(k=2, prices=[3, 2, 6, 5, 0, 3])from)
