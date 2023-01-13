from collections import Counter as counter
from typing import List, Counter


def minimum_window_substring(s: str, t: str) -> str:
    '''브루트 포스, counter 사용한 풀이'''
    if not t or not s or len(s) < len(t):
        return ""

    required = counter(t)

    for window_size in range(len(t), len(s) + 1):
        for start in range(len(s) - window_size + 1):
            window = s[start:start + window_size]
            if contains(list(window), required):
                return window
    return ""


def contains(substring: List[str], required: Counter) -> bool:
    substring_counter = counter(substring)

    for char, count in required.items():
        if substring_counter[char] < count:
            return False
    return True


def minimum_window_substring2(s: str, t: str) -> str:
    '''투포인터, 슬라이딩 윈도우로 최적화'''
    need = counter(t)
    missing = len(t)
    left = start = end = 0

    for right, char in enumerate(s, 1):
        missing -= (need[char] > 0)
        need[char] -= 1

        if missing > 0:
            continue

        while left < right and need[s[left]] < 0:
            # 아래 두줄 순서 바뀌니 틀림
            left += 1
            need[s[left]] += 1

        if not end or right - left <= end - start:
            start, end = left, right

        need[s[left]] += 1
        missing += 1
        left += 1

    return s[start:end]


def minWindow(s: str, t: str) -> str:
    need = counter(t)
    missing = len(t)
    left = start = end = 0

    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1

        # 필요 문자가 0이면 왼쪽 포인터 이동 판단
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1

            if not end or right - left <= end - start:
                start, end = left, right

            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]


# print(minimum_window_substring("ADOBECODEBANC", "ABC"))
# print(minimum_window_substring2("ADOBECODEBANC", "ABC"))
print(minimum_window_substring("ABCDEFUCKYOU", "CK"))
print(minimum_window_substring("ABFCCB", "BC"))
print(minimum_window_substring2("ABCDEFUCKYOU", "CK"))
print(minimum_window_substring2("ABFCCB", "BC"))
print(minWindow("ABCDEFUCKYOU", "CK"))
print(minWindow("ABFCCB", "BC"))
# print(minimum_window_substring("ABCDEFUCKYOU", "CK"))
# print(minimum_window_substring("ADOBECODEBANC", ""))
# print(minimum_window_substring("", "ABC"))
# print(minimum_window_substring("DEF", "ABC"))
