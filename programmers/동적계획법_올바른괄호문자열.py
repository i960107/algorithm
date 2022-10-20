from typing import Final


class Bracket:
    EMPTY: Final = -1
    INFINITY: Final = -1000

    def __init__(self, brackets: str):
        self.n = len(brackets)
        self.brackets = brackets
        self.memo = [[self.EMPTY] * self.n for _ in range(self.n)]

    def is_paired(self, left_index: int, right_index: int) -> bool:
        return (self.brackets[left_index] == "(" and self.brackets[right_index] == ")") or (
                self.brackets[left_index] == "[" and self.brackets[right_index] == "]")

    # 부분 문자열 brackets[left_most: right_most + 1] 에 대한 가장 긴 올바른 괄호 문자열의 길이
    def get_longest_valid_bracket(self, left_most: int, right_most: int) -> int:

        if left_most < 0 or right_most >= self.n or left_most > right_most:
            print("잡았다")
            return 0

        elif self.memo[left_most][right_most] != self.EMPTY:
            return self.memo[left_most][right_most]

        elif left_most == right_most:
            # 한 글자는 괄호 문자열이 될 수 없다
            return 0

        answer = 0

        # 양쪽 끝이 짝이 맞는 경우, 해당 괄호짝이 감싼 경우를 고려한다.
        if self.is_paired(left_most, right_most):
            answer = 2 + self.get_longest_valid_bracket(left_most + 1, right_most - 1)

        for mid in range(left_most, right_most):
            left_length = self.get_longest_valid_bracket(left_most, mid)
            right_length = self.get_longest_valid_bracket(mid + 1, right_most)
            total_length = left_length + right_length
            answer = max(answer, total_length)

        self.memo[left_most][right_most] = answer

        return answer


for _ in range(int(input())):
    b = Bracket(input())
    print(b.get_longest_valid_bracket(0, b.n - 1))
