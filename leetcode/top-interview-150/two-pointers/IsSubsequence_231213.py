from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str):
        if not s:
            return True
        pos = 0
        # pos index out of range 체크해야함.
        # 빈 배열인 경우?
        for c in t:
            if c == s[pos]:
                pos += 1
                if pos == len(s):
                    return True

        return False

s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdc"))
print(s.isSubsequence("abcde", "abc"))
print(s.isSubsequence("abcde", ""))
print(s.isSubsequence("", "abc"))
