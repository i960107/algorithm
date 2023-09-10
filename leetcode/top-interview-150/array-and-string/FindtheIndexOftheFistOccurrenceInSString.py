from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return - 1
        start = []
        for index, c in enumerate(haystack):
            if c == needle[0]:
                start.append(index)

        for s in start:
            if s + len(needle) - 1 >= len(haystack):
                continue
            found = True
            for k in range(len(needle)):
                if haystack[s + k] != needle[k]:
                    found = False
                    break
            if found:
                return s
        return - 1


s = Solution()
print(s.strStr(haystack="sadbutsad", needle="sad"))
print(s.strStr(haystack="leetcode", needle="leeto"))
print(s.strStr(haystack="badbutsad", needle="sad"))
print(s.strStr(haystack="sa", needle="sa"))
print(s.strStr(haystack="a", needle="sa"))
