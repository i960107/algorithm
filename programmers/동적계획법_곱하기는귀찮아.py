from typing import List, Final
from sys import stdin


class Matrix:
    def __init__(self, row_size: int, column_size: int):
        self.row_size = row_size
        self.column_size = column_size


class MatrixMultiplication:
    EMPTY: Final = -1
    INFINITY = 1000000000

    def __init__(self, n: int, matrices: List[Matrix]):
        self.n = n
        self.matrices = matrices
        self.memo = [[self.EMPTY] * n for _ in range(n)]

    # matrices[left_most ... right_most] 범위의 모든 행렬을 곱할 때 발생하는 최소의 곱하기 연산의 수
    # left_most, right_most : 가장 왼쪽 끝 오른쪽 끝 인덱스
    def get_min_multiplication(self, left_most: int, right_most: int) -> int:

        if left_most < 0 or right_most >= n or left_most > right_most:
            return self.INFINITY

        elif self.memo[left_most][right_most] != self.EMPTY:
            return self.memo[left_most][right_most]

        elif left_most == right_most:
            return 0

        answer = self.INFINITY

        # [left_most, mid]와 [mid, right_most]로 나누었을때
        for mid in range(left_most, right_most):

            left_cost = self.get_min_multiplication(left_most, mid)
            right_cost = self.get_min_multiplication(mid + 1, right_most)

            # 좌우 영역을 모두 곱하는데 소모되는 비용
            concat_cost = self.matrices[left_most].row_size * self.matrices[mid].column_size * self.matrices[
                right_most].column_size

            total_cost = left_cost + right_cost + concat_cost

            answer = min(total_cost, answer)

        self.memo[left_most][right_most] = answer

        return answer

    # 배열으로 주어진 행렬이 모두 곱하기가 가능한지 판단하는 함수
    def is_multipliccable(self) -> bool:

        for i in range(self.n - 1):

            if matrices[i].column_size != matrices[i + 1].row_size:
                return False

        return True


t = int(input())

read = stdin.readline

for _ in range(t):
    n = int(read())
    arr = list(map(int, read().split()))
    matrices = [Matrix(arr[i], arr[i + 1]) for i in range(0, len(arr), 2)]
    m = MatrixMultiplication(n, matrices)

    if m.is_multipliccable():
        print(m.get_min_multiplication(0, n - 1))
    else:
        print(-1)
