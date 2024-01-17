from typing import List


class Solution:
    # 거래가 여러번 일어날 수 있다. 단, 한번에 한주만.
    # transaction 제한 없음.
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # 값이 어제보다 올랐다면 거래한다.
        # greedy 아니고 dp인 이유.
        # 전체 수익을 얻기 위해서 이전 날까지의 최대 수익을 활용한다. subproblem 최적 부분구조. repeated question(재귀적으로 계속 전날계산)
        # greedy가 아닌 이유.
        # profit은 0  i-1까지 얻은 최대 수익. tabulation해가는 것.
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit

    # 다음번 값이 오르면 사소 다음 번 값이 내리면 판다 매 단계마다 이익을 취한다 -> 탐욕.
    def maxProfit2(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        return result


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
