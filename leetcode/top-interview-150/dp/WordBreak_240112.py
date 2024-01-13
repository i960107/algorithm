from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i - len(word) < 0 or not dp[i - len(word)]:
                    continue
                if s[i - len(word):i] == word:
                    dp[i] = True
                    break
        return dp[len(s)]


s = Solution()
print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(s.wordBreak(s="leetcode", wordDict=["leet", "cod"]))
print(s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
