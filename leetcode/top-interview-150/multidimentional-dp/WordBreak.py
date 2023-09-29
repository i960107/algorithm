from collections import defaultdict
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        temp = ''
        for c in s:
            temp += c
            if temp in wordSet:
                temp = ''
        return temp == ''

    # 트라이? 나눌 수 있는 경우가 여러가지 인경우 현재 단어가 나눠진다고 해서 바로 선택하면 안됨
    # def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
    #     root = dict()
    #     EOW = "EOW"
    #     for word in wordDict:
    #         curr = root
    #         for c in word:
    #             if c not in curr:
    #                 curr[c] = dict()
    #             curr = curr[c]
    #         curr[EOW] = True
    #
    #     curr = root
    #     index = 0
    #     while True:
    #         if s[index] in curr:
    #             curr = curr[s[index]]
    #             index += 1
    #         else:
    #             return False

    # range DP?
    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [[False] * len(s) for _ in range(len(s))]


s = Solution()
print(s.wordBreak(s="leetcode", wordDict=["leets", "code"]))
# 나눌수 있는 경우가 여러가지 인 경우도 포함해야함.
print(s.wordBreak(s="leetcode", wordDict=["leetc", "leet", "ode"]))
print(s.wordBreak(s="aaaaaaa", wordDict=["aaaa", "aaa"]))
print(s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
