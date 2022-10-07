from typing import List, Final
from sys import stdin


class RangeSum:
    EMPTY: Final = -10001

    def __init__(self, n: int, values: List[List[int]]):
        self.n = n
        self.values = values
        self.memo = [[self.EMPTY] * n for _ in range(n)]

    def get_range_sum(self, last_row: int, last_col: int) -> int:
        if last_row < 0 or last_col < 0:
            return 0

        elif self.memo[last_row][last_col] != self.EMPTY:
            return self.memo[last_row][last_col]

        elif last_row == 0 and last_col == 0:
            self.memo[0][0] = values[last_row][last_col]
            return values[last_row][last_col]

        answer = self.get_range_sum(last_row - 1, last_col) \
                 + self.get_range_sum(last_row, last_col - 1) \
                 - self.get_range_sum(last_row - 1, last_col - 1) \
                 + self.values[last_row][last_col]

        self.memo[last_row][last_col] = answer

        return answer


n, m = map(int, input().split())

values = []
for _ in range(n):
    values.append(list(map(int, input().split())))

rs = RangeSum(n, values)

for _ in range(m):
    min_row, min_col, max_row, max_col = map(lambda x: x - 1, map(int, input().split()))
    case1 = rs.get_range_sum(max_row, max_col)
    case2 = rs.get_range_sum(min_row - 1, max_col)
    case3 = rs.get_range_sum(max_row, min_col - 1)
    case4 = rs.get_range_sum(min_row - 1, min_col - 1)
    res = case1 - case2 - case3 + case4
    print(res)

