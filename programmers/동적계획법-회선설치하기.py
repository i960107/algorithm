from typing import List, Final, Tuple
from sys import stdin


class LineInstall:
    EMPTY: Final = -1
    # 불가능한 값
    INFINITY: Final = 1000 * (99 + 99) + 1

    def __init__(self, n: int, difficulties: List[List[int]]):
        self.n = n
        self.difficulties = difficulties
        self.memo = [[self.EMPTY] * n for _ in range(n)]

    def get_min_difficulties(self, r: int, c: int) -> int:

        if r < 0 or c < 0:
            return self.INFINITY

        elif self.memo[r][c] != self.EMPTY:
            return self.memo[r][c]

        if r == 0 and c == 0:
            answer = difficulties[r][c]

        else:
            answer = min(self.get_min_difficulties(r - 1, c), self.get_min_difficulties(r, c - 1)) \
                     + self.difficulties[r][c]

        self.memo[r][c] = answer

        return answer


n = int(input())

# 빠른 입력을 위해
read = stdin.readline

difficulties = []
for _ in range(n):
    difficulties.append(list(map(int, read().split())))

li = LineInstall(n, difficulties)
res = li.get_min_difficulties(n - 1, n - 1)
print(res)
