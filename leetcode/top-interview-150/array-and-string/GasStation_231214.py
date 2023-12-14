from typing import List


class Solution:
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    # n = len(gas)
    # # prefix sum이 아니라 지나치는 모든 곳에서 < 0이 한번이라도 되면 안됨.
    # dp = [gas[i] - cost[i] for i in range(n)]
    # print(dp)
    # min_prefix, end = float('INF'), None
    # for i in range(1, n):
    #     dp[i] += dp[i - 1]
    #     if dp[i] < min_prefix:
    #         min_prefix = dp[i]
    #         end = i
    # print(dp)
    # # dp = [-2, -2, -2, 3, -3, 6] 이면 정답은 3이 아니라 5여야 한다.
    # for start in range(end + 1, n):
    #     if
    # # i를 시작포인트로 누적합이 한번이라도 음수가 되지 않는 i를 찾는다.
    # # i번째를 시작으로 한 누적합은 i -1을 시작으로 한 누적합에서 dp[i-1]을 뺀 것 아닌가.
    # # gas 가 0이면 출발할 수 없고 gas < cost이면 나아갈 수 없다.

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        deficit = balance = start = 0
        n = len(gas)
        for i in range(n):
            balance += gas[i] - cost[i]
            if balance < 0:
                deficit += balance
                start = i + 1
                balance = 0
            if deficit + balance >= 0:
                return start
        return - 1


s = Solution()
print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
print(s.canCompleteCircuit([1, 6, 0, 6, 0], [0, 3, 4, 3, 3]))
