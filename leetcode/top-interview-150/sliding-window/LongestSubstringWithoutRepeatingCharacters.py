from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0

        # 마지막으로 등장한 인덱스.
        used = dict()

        for end, char in enumerate(s):
            if char in used and used[char] >= start:
                start = used[char] + 1
            else:
                max_length = max(max_length, end - start + 1)
            used[char] = end
        return max_length

    def solution2(self, s: str) -> int:
        max_len = -float('inf')

        l = 0
        d = defaultdict(int)
        duplicated = 0

        for r in range(len(s)):
            chr = s[r]
            if d[chr] > 0:
                duplicated += 1
            d[chr] += 1

            if duplicated == 0 and r - l + 1 > max_len:
                max_len = r - l + 1

            while duplicated > 0:
                d[s[l]] -= 1
                if d[s[l]] == 1:
                    duplicated -= 1
                l += 1

        return max_len if max_len > 0 else 0


s = Solution()
# print(s.solution2("abcabcbb"))
# print(s.solution2("bbbbbbb"))
# print(s.solution2("pwwkew"))
# print(s.solution2("12ab c2a."))
# print(s.solution2("12abc ,"))
# print(s.solution2(""))
print(s.solution2("nfpdmpi"))
