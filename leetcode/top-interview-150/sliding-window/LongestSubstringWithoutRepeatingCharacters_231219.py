from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, included = 0, dict()
        max_len = 0
        # left pointer 옮기면서 그 전 글자들 다 included에서 삭제해주어야함.
        for r in range(n):
            if s[r] in included and included[s[r]] >= l:
                l = included[s[r]] + 1
            included[s[r]] = r
            if r - l + 1 > max_len:
                max_len = r - l + 1
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring(s="pwwkew"))
print(s.lengthOfLongestSubstring(s="abcabcbb"))
print(s.lengthOfLongestSubstring(s="bbbbb"))
print(s.lengthOfLongestSubstring(s="abba"))
print(s.lengthOfLongestSubstring(s=""))
