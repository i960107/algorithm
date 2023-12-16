from collections import Counter


class Solution:
    # answer is unique ?
    # substring character order does not matter
    # Could you find an algorith, that runs in O(M+N) time?
    def minWindow(self, s: str, t: str) -> str:
        start, end = 0, 0

        required = Counter(t)
        missing = len(required)

        while end < len(s):
            curr = s[end]
            required[curr] -= 1
            if required[curr] == 0:
                missing -= 1
            if missing == 0:
                break
            end += 1

        # s[start: end + 1]
        if missing > 0:
            return ""

        left, right = start, end
        while True:
            required[s[left]] += 1
            if required[s[left]] == 1:
                missing += 1
            left += 1

            if right + 1 < len(s):
                right += 1
                required[s[right]] += 1
                if required[s[left]] == 1:
                    missing += 1

        # end  -start window size는 바뀜
        return s[start:end + 1]


s = Solution()
print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
