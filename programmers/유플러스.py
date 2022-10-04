from typing import List
from math import log2
from collections import Counter


def get_anagram_group_count(arr: List[int]) -> int:
    anagrams = Counter([''.join(sorted(str(x))) for x in arr])
    return len(anagrams)


# print(get_anagram_group_count([112, 1814, 121, 1481, 1184]))


def get_original_from_compressed(compressed: str) -> str:
    stack = []
    i = 0

    while i < len(compressed):

        if compressed[i].isdigit():

            stack.append(compressed[i])
            while compressed[i + 1].isdigit():
                stack[-1] += compressed[i + 1]
                i += 1

        elif compressed[i] == "(":
            pass

        elif compressed[i] == ")":
            repeated = stack.pop() * int(stack.pop())
            if not stack or stack[-1].isdigit():
                stack.append(repeated)
            else:
                stack[-1] += repeated
        else:
            if not stack or stack[-1].isdigit():
                stack.append("")
            stack[-1] += compressed[i]

        i += 1

    # return ''.join(stack)
    return stack.pop()


# print(get_original_from_compressed("abcdef"))
# print(get_original_from_compressed("2(2(hi)2(co))x2(bo)"))
# print(get_original_from_compressed("10(p)"))
# print(get_original_from_compressed("2(3(hi)co)"))
# print(get_original_from_compressed("2(2(2(a)b)c)"))


def get_max_special_match_count(players: List[int]) -> int:
    matches = [0] * int(2 ** (log2(len(players)) + 1) - 1)

    for i in range(len(players)):

        match = len(matches) - len(players) + i

        if players[i]:
            while match != 0:
                matches[match] = 1
                match = (match - 1) // 2
            matches[0] = 1

    def _print():
        i = 0
        while i < len(matches):
            print(matches[i:i * 2 + 1])
            i = i * 2 + 1

    # 탐욕법? 합이 더 작은 걸 찾아가면 되나?
    def replace():
        i = 0
        while i < len(matches) - len(players):
            matches[i] = 1
            if not matches[i * 2 + 1]:
                i = i * 2 + 1
            else:
                i = i * 2 + 2

    replace()
    _print()

    def get_special_match_count() -> int:
        return sum(matches[:-len(players)])

    return get_special_match_count()


# print(get_max_special_match_count([1, 0, 0, 1, 0, 0, 1, 0]))
print(get_max_special_match_count([0, 0, 1, 0, 0, 0, 0, 0]))
print(get_max_special_match_count([1, 1, 1, 1, 1, 1, 1, 1]))
