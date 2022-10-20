from typing import List, Final


class Item:
    # value: 가격, cost: 무게
    def __init__(self, cost: int, value: int):
        self.cost = cost
        self.value = value


class Knapsack:
    EMPTY: Final = -1
    INFINITY: Final = -1000000000

    def __init__(self, n: int, capacity: int, items: List[Item]):
        self.n = n
        self.capacity = capacity
        self.items = items
        # memo[i][j] := items[0..i]의 보석들 중에서 j만큼의 무게를 사용해서 얻을 수 있는 최대 가치
        self.memo = [[self.EMPTY] * (capacity + 1) for _ in range(n)]

    # items[0..lastItemIndex]의 보석만들 고려하여 정확히 TotalCost의 무게를 채웠을때 얻을 수 있는 최대 가치
    # lastItemIndex : 마지막 보석의 인덱스
    # totalCost : 사용할 모든 보석의 무게 합
    def get_max_profit(self, last_item_index: int, total_cost: int) -> int:
        if last_item_index < 0 or total_cost < 0 or total_cost > self.capacity:
            # 불가능한 경우
            return self.INFINITY
        elif self.memo[last_item_index][total_cost] != self.EMPTY:
            return self.memo[last_item_index][total_cost]
        elif total_cost == 0:
            # 더 이상 아무 보석도 담을 수 없는 경우
            return 0

        # 이번 아이템을 사용하지 않는 경우
        answer = self.get_max_profit(last_item_index - 1, total_cost)

        # 이번 아이템을 사용하는 경우
        if self.items[last_item_index].cost <= total_cost:
            prev_cost = total_cost - self.items[last_item_index].cost
            prev_value = self.get_max_profit(last_item_index - 1, prev_cost)
            curr_value = prev_value + self.items[last_item_index].value
            answer = max(answer, curr_value)

        self.memo[last_item_index][total_cost] = answer
        return answer


n, c = map(int, input().split())

items = []

for _ in range(n):
    items.append(Item(*map(int, input().split())))

ks = Knapsack(n, c, items)
answer = 0
for total_cost in range(0, c + 1):
    answer = max(answer, ks.get_max_profit(n - 1, total_cost))
print(answer)

# # 쓴 무게, 가격
# dp = [[] for _ in range(n)]
# # 왜 dp = [[] * n 이 안되지]
# dp[0] = (jewelry[0][0], jewelry[0][1])
#
# for i in range(1, n):
#     if c - dp[i - 1][0] >= jewelry[i][0]:
#         dp[i] = [1]
#         dp[i] = [dp[i - 1][0] + jewelry[i][0], dp[i - 1][1] + jewelry[i][1]]
#
#     else:
#         if dp[i - 1][1] > jewelry[i][1]:
#             dp[i] = dp[i - 1]
#         else:
#             dp[i] = jewelry[i]
#
# print(dp[-1][1])
