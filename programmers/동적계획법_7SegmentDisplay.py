from typing import List, Final


class Item:
    def __init__(self, value: int, cost: int):
        self.value = value
        self.cost = cost


class Knapsack:
    EMPTY: Final = -1

    # 한자리로 표현할 수 있는 수의 개수, 표현할 수 있는 최대 수
    def __init__(self, n: int, capacity: int, items: List[Item]):
        self.n = n
        self.capacity = capacity
        self.items = items
        self.memo = [self.EMPTY] * (capacity + 1)

    def f(self, total_cost: int) -> int:
        if total_cost < 0 or total_cost > self.capacity:
            # return self.EMPTY
            return 0

        elif self.memo[total_cost] != self.EMPTY:
            return self.memo[total_cost]

        elif total_cost == 0:
            # 세그먼트를 모두 사용한 경우의 수 하나 추가
            return 1

        ways = 0
        for n in range(10):
            # 마지막 글자가 last digit인 경우의 수 모두 누적
            ways += self.f(total_cost - self.items[n].cost)

        self.memo[total_cost] = ways

        return ways


items = []

SEGMENTS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
MAX_SEGMENTS = 500000

for n in range(10):
    items.append(Item(n, SEGMENTS[n]))

ks = Knapsack(10, MAX_SEGMENTS, items)

t = int(input())
for _ in range(t):
    total_segments = int(input())

    if not total_segments:
        print(0)
    else:
        answer = ks.f(total_segments)

        # 맨 앞글자가 0인 문자열은 제외
        if total_segments > items[0].cost:
            answer -= ks.f(total_segments - items[0].cost)

        print(answer)
