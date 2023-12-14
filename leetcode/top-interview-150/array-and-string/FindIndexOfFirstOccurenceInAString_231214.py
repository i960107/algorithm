class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for start in range(len(haystack)):
            i, j = start, 0
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return start
        return -1


s = Solution()
print(s.strStr("sadbutsad", "sad"))
print(s.strStr("a", "a"))
print(s.strStr("aaaa", "a"))
print(s.strStr("aaaa", "aaaaa"))
