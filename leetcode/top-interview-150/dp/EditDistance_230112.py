from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        if not n or not m:
            return max(n, m)

        # dp[i][j] : word1[:i + 1] word2[j +1] 사이의 minDistance
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for j in range(1, m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(
                    dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1),  # 마지막 글자 replace
                    dp[i][j - 1] + 1,  # insert
                    dp[i - 1][j] + 1)  # delete
                # if word1[i] == word2[j]:
                #     dp[i][j] = min(
                #         dp[i - 1][j - 1],  # 그대로
                #         dp[i][j - 1] + 1,  # insert
                #         dp[i - 1][j] + 1)  # delete
                # else:
                #     dp[i][j] = min(
                #         dp[i - 1][j - 1] + 1,  # 마지막 글자 replace
                #         dp[i][j - 1] + 1,  # insert
                #         dp[i - 1][j] + 1)  # delete

        return dp[n][m]


s = Solution()
print(s.minDistance(word1="horse", word2="ros"))
print(s.minDistance(word1="", word2="ros"))
print(s.minDistance(word1="horse", word2=""))
print(s.minDistance(word1="intention", word2="execution"))
print(s.minDistance(word1="pneumonoultramicroscopicsilicovolcanoconiosis", word2="ultramicroscopically"))
