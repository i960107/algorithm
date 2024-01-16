from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)
        # n + m = l임.
        if n + m != l:
            return False
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                break
        for j in range(1, m + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                break

        # 나눠진 덩어리 수가 비슷해야함(같거나 하나차이) -> 무조건 그렇게 됨. 덩어리가 두개니깐.
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         if (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or \
        #                 (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]):
        #             dp[i][j] = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]
        return dp[n][m]

    # top - down
    # 빈문자열인 경우..
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        @cache
        def dp(i: int, j: int) -> bool:
            if i < 0 and j < 0:
                return True

            result = False
            if i >= 0 and s1[i] == s3[i + j + 1]:
                result |= dp(i - 1, j)
            if j >= 0 and s2[j] == s3[i + j + 1]:
                result |= dp(i, j - 1)
            return result

        return dp(m - 1, n - 1)


# 글자를 다 써야하는게 아닌가?
s = Solution()
# print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
# print(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
# print(s.isInterleave(s1="", s2="", s3=""))
# print(s.isInterleave(s1="a", s2="b", s3="a"))
# print(s.isInterleave(s1="ac", s2="b", s3="ab"))
print(s.isInterleave(s1="aabc", s2="abad", s3="aabadabc"))
