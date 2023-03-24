from typing import List
from collections import Counter


# 시간 초과 날거 같더라니... dp풀이
# def solution(gems: List[str]) -> List[int]:
#     # 진열대의 대수
#     n = len(gems)
#     gem_dict = dict()
#
#     dp = [[0] * n for _ in range(n)]
#     for i, gem in enumerate(gems):
#         if gem not in gem_dict:
#             gem_dict[gem] = len(gem_dict)
#         dp[i][i] = 1 << gem_dict[gem]
#     gem_n = len(gem_dict)
#
#     def _dp(left: int, right: int) -> int:
#         if dp[left][right]:
#             return dp[left][right]
#         mid = (left + right) // 2
#         left_included = _dp(left, mid)
#         right_included = _dp(mid + 1, right)
#         dp[left][right] = left_included | right_included
#         dp[right][left] = left_included | right_included
#         return dp[left][right]
#
#     # 체크되지 않는 구간 있음.
#     for left in range(n):
#         for right in range(left + 1, n):
#             _dp(left, right)
#     # _dp(0, n - 1)
#     for row in dp:
#         print(row)
#
#     start, end = 0, n - 1
#     full_included = (1 << (gem_n)) - 1
#     # 모든 보석을 포함하는 가장 짧은 구간
#     for s in range(n):
#         for e in range(s, n):
#             if dp[s][e] == full_included and end - start > e - s:
#                 start, end = s, e
#     return [start + 1, end + 1]

# 투포인터로 가능할까?
# 어떤 경우에 실패하지?
# 포인터 늘려가기, 포인터 줄여가기
# 비슷한 문제? -> 부분 문자열이 포함된 최소 윈도우!
def solution(gems: List[str]) -> List[int]:
    # left, right포인터가 뒤집어지는 경우는 없나?
    n = len(gems)
    final_left, final_right = 0, n - 1

    gem_n = len(set(gems))

    def _solution(start: int, end: int):
        counter = Counter(gems[start:end])
        if len(counter) != gem_n:
            return

        left, right = start, end

        while True:
            left_gem = gems[left]
            right_gem = gems[right]

            # 언제 반복문 종료?
            if counter[left_gem] == 1 and counter[right_gem] == 1:
                break

            # 어떻게 시작 진열대 번호가 가장 짧게?
            # 왼쪽, 오른쪽 같은 보석이라면 오른쪽 포인터 먼저 옮기기
            # 한번에 한 포인트 씩만 옮기기
            if counter[right_gem] > 1:
                counter[right_gem] -= 1
                right -= 1

            # 세개 다 같은 경우..
            elif counter[left_gem] > 1:
                counter[left_gem] -= 1
                left += 1

        nonlocal final_left, final_right
        if final_right - final_left > right - left:
            final_left, final_right = left, right

    for start in range(n):
        _solution(start, n - 1)

    return [final_left + 1, final_right + 1]


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["XYZ", "XYZ", "XXX"]))
print(solution(["XYZ", "XXX", "XYZ"]))
print(solution(["X", "Y", "Z"]))
print(solution(["X"]))
