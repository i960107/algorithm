from typing import List


class Solution:
    # brute-force -> 중복된 하위문제 제거 dp
    def longestPalindrome(self, s: str) -> str:
        dp = [[None] * len(s) for _ in range(len(s))]
        # lps = ""
        # for start in range(len(s)):
        #     for end in range(start + 1, len(s)):
        #         if s[start] != s[end]:
        #             continue
        #         res = True
        #         if start + 1 < end - 1:
        #             # 아직 계산 안 되었을 확률 없나? 있는데..
        #             res = dp[start + 1][end - 1]
        #         dp[start][end] = res
        #         dp[end][start] = res
        #         lps = s[start:end + 1]

        ans = ""

        # dp memoization 하려고 했는데 (0,7) (1,6) ...으로 불러지지 (2,4)는 호출되지 않아서 망했음..
        def lps(start: int, end: int) -> bool:
            if start > end:
                return True
            if dp[start][end] != None:
                return dp[start][end]
            # 호출 끝나버림.
            res = False
            nonlocal ans
            if lps(start + 1, end - 1) and s[start] == s[end]:
                res = True
            dp[start][end] = res
            if dp[start][end] and end - start + 1 > len(ans):
                ans = s[start: end + 1]
            return dp[start][end]

        # s[i:i+1]도 palindrome임.
        for i in range(len(s)):
            for j in range(i, len(s)):
                lps(i, j)

        return ans

    def longestPalindrome2(self, s: str) -> str:
        # 중복문제를 줄일 수 있나? 중복문제가 없음!
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 왜 left + 1?
            # while문을 빠져나온 상태에서는 s[left] != s[right]인 상태.
            return s[left + 1:right]

        ans = ""
        # i로부터 시작하는 가장 긴 palindrome찾기.
        for i in range(len(s) - 1):
            # 왜 두글자, 세글자를 기준으로 expand.
            # 자기자신인 경우는 포함됨.
            # palindrome은 짝수개 혹은 홀수개가 될 수 있다.
            ans = max(ans, expand(i, i + 1), expand(i, i + 2), key=len)
        return ans


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("asdecbbdads"))
print(s.longestPalindrome("abcddcba"))
