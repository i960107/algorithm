from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = dict()

        # day1에 사고 day2에 파는 경우의 max_profit ? O
        # day1과 day2사이의 최대 profit ? -> 두번 거래 제한할 수 없음.
        # at most two transactions. transction이 안 일어나는게 나을 수도 있음.
        def dp(day1: int, day2: int):
            if day1 >= day2:
                return 0
            if day1 + 1 == day2:
                return max(0, prices[day2] - prices[day1])
            if (day1, day2) not in cache:
                max_profit = 0
                # maximum recursion error 발생
                for mid in range(day1 + 1, day2):
                    profit = dp(day1, mid) + dp(mid + 1, day2)
                    if profit > max_profit:
                        max_profit = profit
                cache[(day1, day2)] = max_profit

            return cache[(day1, day2)]

        dp(0, n - 1)
        for day1 in range(n):
            for day2 in range(n):
                print(cache[(day1, day2)])

        return cache[(0, n - 1)]


s = Solution()
# print(s.maxProfit([3, 1, 3, 4]))
print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
