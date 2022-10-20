from typing import List, Final


class AhChoo:
    EMPTY: Final = -1

    def __init__(self, n: int, signA: List[int], signB: List[int]):
        self.n = n
        self.signA = signA
        self.signB = signB
        self.memo = [[self.EMPTY] * n for _ in range(n)]

    # i: signA의 부분집합의 마지막 인덱스
    # j: signB의 부분집합의 마지막 인덱스
    # 두 부분 파형 X[:i+1]와 Y[:j+1]사이의 최소 거리

    def get_min_distance(self, i: int, j: int) -> int:

        if i < 0 or j < 0:
            return 1000 * 1000 + 1

        elif self.memo[i][j] != self.EMPTY:
            return self.memo[i][j]

        # 시점이 하나씩밖에 없는 경우 서로 대응된다
        elif i == j == 0:
            diff = self.signA[0] - self.signB[0]
            self.memo[0][0] = diff ** 2
            return self.memo[0][0]

        # 해당 두 시점 차의 값.
        # 모든 시점은 하나 이상의 값과 대응되어야하며, 교차될 수 없기 때문에  i - j는 무조건 연결
        diff = self.signA[i] - self.signB[j]

        # 해당 두 시점 이전 시점들의 대응들에 대한 최적해와 더한다
        answer = self.memo[i][j] = min(
            self.get_min_distance(i - 1, j),
            self.get_min_distance(i, j - 1),
            self.get_min_distance(i - 1, j - 1)
        ) + diff ** 2

        self.memo[i][j] = answer
        return self.memo[i][j]


n = int(input())
signA = list(map(int, input().split()))
signB = list(map(int, input().split()))

ac = AhChoo(n, signA, signB)
print(ac.get_min_distance(n - 1, n - 1))

