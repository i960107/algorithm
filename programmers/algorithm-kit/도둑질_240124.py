from typing import List


# circular 관련된 문제
# 1. Maximum Sum Subarray Circular
# 2. House Robber circular

def solution(money: List[int]) -> int:
    if len(money) <= 2:
        return max(money)
    # def _rob(start: int) -> int:
    #     dp = [0] * len(money)
    #     for i in range(len(money)):
    #         curr = (i + start) % len(money)
    #         prev = (i + start - 1) % len(money)
    #         prev_prev = (i + start - 2) % len(money)
    #         dp[(i + start) % len(money)] = dp[(i + start - 2) % len(money)] +
    #
    # max_money = 0
    # for i in range(len(money)):
    #     result = _rob(i)
    #     if result > max_money:
    #         max_money = result
    # return max_money

    n = len(money)

    dp1 = [0] * (n - 1)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    dp2 = [0] * n
    dp2[1] = money[1]
    dp2[2] = max(money[1], money[2])
    for i in range(3, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(dp1[-1], dp2[-1])


def solution2(money: List[int]) -> int:
    def helper(nums):
        rob1, rob2 = 0, 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

    return max(money[0], helper(money[:-1]), helper(money[1:]))


print(solution([2, 3, 2]))  # 3
