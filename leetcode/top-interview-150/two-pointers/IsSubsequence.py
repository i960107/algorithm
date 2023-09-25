from typing import List


# 둘다 빈 문자열이 될 수 있다.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        tp = 0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        return sp == len(s)


s = Solution()
print(s.isSubsequence(s="abc", t="ahbgdc"))
print(s.isSubsequence(s="axc", t="ahbgdc"))
