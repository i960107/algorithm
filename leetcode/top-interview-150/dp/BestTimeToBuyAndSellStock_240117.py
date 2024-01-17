from typing import List


class Solution:
    # 거래가 한번만 일어나야한다.
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = [p for p in prices]
        # 이부분이 dp. 0  ~ i까지의 최대값은 0 ~ i-1까지의 최대값과 현재 값 중 더 작은 값.
        # subproblem.  -> memoization방식. 만약 repeated question으로 풀면 tabulation이 됨.
        # 이건 tabulation방식.
        for i in range(1, n):
            if min_price[i - 1] < min_price[i]:
                min_price[i] = min_price[i - 1]

        answer = 0
        for i in range(1, n):
            if prices[i] - min_price[i - 1] > answer:
                answer = prices[i] - min_price[i - 1]
        return answer

    def maxProfitShort(self, prices: List[int]) -> int:
        min_price = prices[0]
        answer = 0
        for i in range(1, len(prices)):
            if prices[i] - min_price > answer:
                answer = prices[i] - min_price
            if min_price > prices[i]:
                min_price = prices[i]

        return answer


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfitShort([7, 1, 5, 3, 6, 4]))
