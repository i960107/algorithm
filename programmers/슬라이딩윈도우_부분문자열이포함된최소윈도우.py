from typing import List
from collections import Counter


def minimum_window_substring_brute_force(S: str, T: str) -> str:
    '''모든 윈도우 크기를 브루트 포스로 계산'''

    # 최악 O(N^2*K^2)
    def contains(s_sub: List, t_sub: List) -> bool:
        for t_elem in t_sub:
            if t_sub in s_sub:
                # 중복 모두 제거되는 것 아님
                s_sub.remove(t_elem)
            else:
                return False
        return True

    if not S or not T:
        return ""

    window_size = len(T)

    for size in range(window_size, len(S) + 1):
        for left in range(len(S) - size + 1):
            s_sub = S[left: left + size]
            if contains(list(s_sub), list(T)):
                return s_sub
    # 못찾음. 포함하고 있지 않음
    return ""


def minimum_window_substring(s: str, t: str) -> str:
    '''투포인터, 슬라이딩 윈도우로 최적화'''
    # O(N)
    # 필요한 문자 각각의 개수
    need = Counter(t)
    # 필요한 문자의 전체 갯수
    missing = len(t)
    left = start = end = 0

    # 오른쪽 포인터를 움직이며 윈도우 결정
    # inex가 1부터 시작, 파이썬의 슬라이싱은 s[n:n+1]의 형태
    for right, char in enumerate(s, 1):
        # 만약 현재 문자가 필요한 문자 need[char]에 포함되어 있다면
        # need[char] > 0 이라면 True가 되어서 -1. 아니면 0
        missing -= need[char] > 0
        # 만약 필요한 무자 아니어도 -= 1. defaultdict인가?
        need[char] -= 1
        # 필요한 문자가 모두 window안에 들어있다면
        # 왼쪽 포인터 최대한 오른쪽 이동
        # need 가 0 이면 오른쪽으로 이동하면 안됨. 0을 가리키는 위치까지이동
        if missing == 0:
            # 만약 left가 불필요한 문자라면
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1

            # left = right이거나 필요한 문자일때 멈춤
            # right - left 이번 loop에서 만든 최소 윈도우
            # 이전 루프까지 최소 윈도우
            # not end인 경우 아직 윈도우 만들어지지 않은 경우
            # 다음 루프 시작은 left 포함하지 않음
            if not end or right - left <= end - start:
                start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1

    return s[start:end]


# print(minimum_window_substring("ADOBECODEBANC", "ABC"))
print(minimum_window_substring("102030123", "123"))


def minimum_window_substring_practice(s: str, t: str) -> str:
    # 예외 처리는 마지막에

    # 필요한 원소 대비 현재 윈도우 안에 문자들이 들어있는 상황
    # value가 양수인 경우 value만큼 더 필요하다
    # value == 0인경우 필요한 만큼 들어있다
    # value가 음수인 경우 value만큼 더 들어있다
    need = Counter(t)
    missing = len(t)

    # start = float('-inf')  end = float('inf') 로 결정해주면
    # 무조건 처음 결정되는 윈도우 사이즈가 end-start보다 작을거기 때문에 따로 체크해줄 필요 없음
    left = start = end = 0
    for right, char in enumerate(s, 1):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        # 윈도우는 결정 -> 포인터 이동
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            # 포인터 결정되었음. 이렇게 결정된 윈도우가 전체에 대해서 최소 윈도우인가?
            # unique한 답이기 때문에 right-left == end-start인 경우 없음
            if not end or right - left < end - start:
                start, end = left, right
                need[s[left]] += 1
                missing += 1
                # left조정해주지 않으면 항상 다음 루프에서는 더 긴 길이의 윈도우 사이즈가 결정됨
                left += 1

    return s[start:end]


# t의 모든 원소가 s에 포함되어 있는 경우
print(minimum_window_substring_practice("102030123", "123"))
# t의 원소 중 일부만 s에 포함되어 있는 경우
print(minimum_window_substring_practice("100301", "123"))
# s 혹은 t가 빈 배열인 경우
print(minimum_window_substring_practice("", "123"))
print(minimum_window_substring_practice("123", ""))
# s의 길이가 t의 길이보다 작은경우
print(minimum_window_substring_practice("1", "123"))
# s의 길이 == t의 길이 인 경우
print(minimum_window_substring_practice("1", "1"))


def minimum_window_counter(s: str, t: str) -> str:
    t_count = Counter(t)
    current_counter = Counter()

    start = float('-inf')
    end = float('inf')

    left = 0
    # 오른쪽 포인터 인동
    for right, char in enumerate(s, 1):
        current_counter[char] += 1
        # missing == 0 대신
        # 만약 요소가 하나라도 비어 있다면 and 연산 결과는 t_count와 일치하지 않을 것
        # and 연산 결과로 왼쪽 포인터 이동 판단
        # 무거운 연산
        # & 결과가 true -> 교집합이 current_counter 가 t를 포함한다.
        while current_counter & t_count == t_count:
            if right - left < end - start:
                start, end = left, right
            current_counter[s[left]] -= 1
            left += 1
    # 유효하지 않은 값일때 start, end가 결정된 적 없을때 체크
    return s[start:end] if end - start <= len(s) else ''


print(minimum_window_counter("102031", "123"))
