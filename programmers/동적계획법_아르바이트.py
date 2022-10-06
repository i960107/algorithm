from typing import List


class PartTime:
    def __init__(self, n: int, incentives: List[int]):
        self.n = n
        self.incentives = incentives
        self.memo = [0] * n

    def get_maximum_incentive(self, last_index: int) -> int:
        if last_index < 0:
            return 0
        elif last_index == 0:
            return self.incentives[0]
        elif last_index == 1:
            return self.incentives[0] + self.incentives[1]


n = int(input())
incentives = list(map(int, input().split()))

pt = PartTime(n, incentives)
res = pt.get_maximum_incentive(n - 1)
print(pt)
