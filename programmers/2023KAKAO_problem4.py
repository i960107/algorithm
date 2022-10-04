from typing import List
from math import log, floor


def solution(numbers: List[int]) -> List[int]:
    def _solution(bin_str: str, is_parent_dummy: bool) -> bool:

        if not bin_str:
            return True

        mid = len(bin_str) // 2

        if is_parent_dummy and bin_str[mid] != "0":
            return False

        left, right = bin_str[:mid], bin_str[mid + 1:]

        if not _solution(left, bin_str[mid] == "0"):
            return False

        if not _solution(right, bin_str[mid] == "0"):
            return False

        return True

    answer = []
    for num in numbers:
        bin_str = bin(num)[2:]
        bin_str = bin_str.ljust(2 * len(bin_str) - 1, "0")
        print(num, bin_str)
        answer.append(int(_solution(bin_str, False)))

    return answer


print(solution([7, 5]))
# print(solution([63, 111, 95]))

# print(bin(1)[2:])
# print(bin(2)[2:])
# print(bin(3)[2:])
# print(bin(4)[2:])
# print(bin(5)[2:])
# print(bin(6)[2:])
# print(bin(7)[2:])
# print(bin(16)[2:])
# print(bin(17)[2:])
# print(bin(32)[2:])
# print(bin(33)[2:])
# print(bin(64)[2:])
# print(bin(65)[2:])
