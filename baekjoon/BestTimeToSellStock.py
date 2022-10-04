from typing import List


def maxProfit(nums: List[int]) -> int:
    buy = 10001
    profit = 0

    for p in nums:
        if p > buy:
            profit += (p - buy)
        buy = p
    return profit


# print(maxProfit([7, 1, 5, 3, 6, 4]))
# print(maxProfit([1, 2, 3, 4, 5]))
# print(maxProfit([7, 6, 4, 3, 1]))

def best_time_to_sell_stock_with_cooldown(prices: List[int]) -> int:
    if len(prices) == 1:
        return 0
    elif len(prices) == 2:
        return max(0, prices[1] - prices[0])
    elif len(prices) == 3:
        return max(0, prices[2] - prices[0], prices[1] - prices[0], prices[2] - prices[1])

    dp = [0] * len(prices)

    dp[1] = max(prices[1] - prices[0], 0)
    dp[2] = max(prices[2] - prices[0], prices[2] - prices[1], 0)

    for i in range(3, len(prices)):
        dp[i] = max(dp[i - 3] + prices[i] - prices[i - 1],
                    dp[i - 2],
                    dp[i - 1])

    return dp[-1]


print(best_time_to_sell_stock_with_cooldown([1, 2, 3, 0, 2]))
print(best_time_to_sell_stock_with_cooldown([1]))
print(best_time_to_sell_stock_with_cooldown([2, 1, 4]))
print(best_time_to_sell_stock_with_cooldown([6, 1, 3, 2, 4, 7]))
