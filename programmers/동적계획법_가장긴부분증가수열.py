from typing import List


def solution(n: int, arr: List[int]) -> int:
    dp = [0] * n

    def _lis(last_index: int) -> int:
        if last_index < 0:
            return 0
        elif last_index == 0:
            dp[last_index] = 1
            return 1
        elif dp[last_index] != 0:
            return dp[last_index]

        lis = 1
        for j in range(last_index):
            if arr[j] <= arr[last_index]:
                lis = max(lis, _lis(j) + 1)
        dp[last_index] = lis
        return lis

    for i in range(n):
        _lis(i)

    print(dp)
    return max(dp)


print(solution(6, [10, 20, 10, 30, 20, 50]))
