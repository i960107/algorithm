from typing import List


class Solution:
    # range dp. dp[i][j] : lenth of longest common subsequence between text1[:i] and text2[:j]
    # 어떻게 구현할 것인가 -> 전체 Iterative하게 채우기. 재귀적으로 필요한 곳만 채우기.
    # 전체 dp 채우기.
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = lcs between dp[i:] and dp[j:]
        # time  and space complexity: O(m * n)
        m, n = len(text1), len(text2)
        # at least one more column is neeeded
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # in reverse order
        # 세로로 탐색하든, 가로로 탐색하든 상관 없음.
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = dp[i + 1][j + 1] + 1
        #         else:
        #             dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

    # 재귀적으로 memoization
    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 0
        for j in range(n + 1):
            dp[m][j] = 0

        def _lcs(i: int, j: int) -> int:
            if dp[i][j] is None:
                if text1[i] == text2[j]:
                    dp[i][j] = _lcs(i + 1, j + 1) + 1
                else:
                    dp[i][j] = max(_lcs(i + 1, j), _lcs(i, j + 1))
            return dp[i][j]

        result = _lcs(0, 0)
        # for row in dp:
        #     print(row)
        return result


s = Solution()
print(s.longestCommonSubsequence("abcde", "ace"))
print(s.longestCommonSubsequence("ace", "abcde"))
print(s.longestCommonSubsequence("abc", "def"))
print(s.longestCommonSubsequence("abcde", "acee"))
print(s.longestCommonSubsequence("pasnw", "vozsh"))
print()
print(s.longestCommonSubsequence2("abcde", "ace"))
print(s.longestCommonSubsequence2("ace", "abcde"))
print(s.longestCommonSubsequence2("abc", "def"))
print(s.longestCommonSubsequence2("abcde", "acee"))
print(s.longestCommonSubsequence2("pasnw", "vozsh"))
print()
print(s.longestCommonSubsequence3("abcde", "ace"))
print(s.longestCommonSubsequence3("ace", "abcde"))
print(s.longestCommonSubsequence3("abc", "def"))
print(s.longestCommonSubsequence3("abcde", "acee"))
print(s.longestCommonSubsequence3("pasnw", "vozsh"))
# m, n = 5, 3
# dp1 = [0 for _ in range(n) for _ in range(m)]
# dp2 = [[0 for _ in range(n)] for _ in range(m)]
# print(dp1)
# print(dp2)
