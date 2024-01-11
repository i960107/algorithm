from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)
        if n + m < l:
            return False
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(1, min(m + 1, l + 1)):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, min(n + 1, l + 1)):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, min(n + 1, l + 1)):
            for j in range(1, min(m + 1, l - i + 1)):
                if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                if dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True

        # what if n + m > l
        found = False
        for i in range(min(n, l + 1)):
            j = l - i
            if l - i <= m and dp[i][j]:
                print(i, j)
                found = True
                break
        return found


s = Solution()
print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
print(s.isInterleave(s1="a", s2="b", s3="a"))
print(s.isInterleave(s1="ac", s2="b", s3="ab"))
