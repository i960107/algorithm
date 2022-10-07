from typing import Final


class LCS:
    EMPTY: Final = -1

    def __init__(self, A: str, B: str):
        self.A = A
        self.B = B
        self.memo = [[self.EMPTY] * len(B) for _ in range(len(A))]

    # 부분 문자열 A[:last_index_a +1]와 B[:last_index_b+1] 사이의 LCS의 길이
    def get_lcs(self, last_index_a: int, last_index_b: int) -> int:
        # 인덱스가 범위를 벗어난 경우
        if last_index_a < 0 or last_index_b < 0:
            return 0

        # 이미 계산된 값이 있는 경우
        elif self.memo[last_index_a][last_index_b] != self.EMPTY:
            return self.memo[last_index_a][last_index_b]

        # A[last_index_a] 를 제외하고 계산한 LCS
        # B[last_index_b] 는 사용될 수 있음
        case1 = self.get_lcs(last_index_a - 1, last_index_b)

        # B[last_index_B] 를 제외하고 계산한 LCS
        # A[last_index_a] 는 사용될 수 있음
        case2 = self.get_lcs(last_index_a, last_index_b - 1)

        # A[last_index_a] B[last_index_b] 를 제외하고 계산한 LCS에 A[last_index_a] B[last_index_b)를 비교한 결과를 더해줌
        case3 = self.get_lcs(last_index_a - 1, last_index_b - 1) + (
            1 if self.A[last_index_a] == self.B[last_index_b] else 0)

        answer = max(case1, case2, case3)
        self.memo[last_index_a][last_index_b] = answer
        return answer


A = input()
B = input()

lcs = LCS(A, B)
res = lcs.get_lcs(len(A) - 1, len(B) - 1)
print(res)
