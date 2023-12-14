from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s = Solution()
print(s.lengthOfLastWord())
