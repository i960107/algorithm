from typing import List


def get_dp(n, m) -> List[int]:
    dp = [0] * len(arr)
    dp[0] = arr[0]
    for i in range(1, len(dp)):
        if arr[i - 1] < arr[i]:
            dp[i] = arr[i - 1]
        else:
            dp[i] = arr[i]

    return dp


def solution(histogram: List[int]) -> int:
    dp = get_dp(histogram)
    print(dp)
    return 0


print(solution([2, 1, 3, 4, 1]))
print(solution([6, 3, 1, 4, 12, 4]))
print(solution([5, 6, 7, 4, 1]))
