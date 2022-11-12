from typing import Final

PAIRS: Final = {
    ")": "(",
    "]": "[",
}

VALUES: Final = {
    "(": 2,
    "[": 3,
}


def solution(brackets: str) -> int:
    if not is_valid_bracket(brackets):
        return 0

    def is_paired(left_index: int, right_index: int) -> bool:
        return (brackets[left_index] == "(" and brackets[right_index] == ")") or (
                brackets[left_index] == "[" and brackets[right_index] == "]")

    def get_score(left_most: int, right_most: int) -> int:

        if left_most < 0 or right_most >= len(brackets) or left_most > right_most:
            return -1

        elif left_most == right_most:
            return -1

        elif right_most - left_most == 1 and is_paired(left_most, right_most):
            score = VALUES[brackets[left_most]]

        else:
            # x와 y의 점수를 합한다
            for mid in range(left_most, right_most, 2):

                left_score = solution(brackets[left_most:mid])
                right_score = solution(brackets[mid + 1: right_most])

                if left_score != -1 and right_score != -1:
                    score = (left_score + right_score) * score
                    break

        return score


def is_valid_bracket(brackets: str) -> bool:
    if not brackets:
        return False

    stack = []
    for b in brackets:

        if b in PAIRS:

            if stack and stack[-1] == PAIRS[b]:
                stack.pop()
            else:
                return False

        else:
            stack.append(b)

    if stack:
        return False

    return True


brackets = input()
print(solution(brackets))
