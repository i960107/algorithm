from typing import List


class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False
        num = str(num)
        i, j = 0, len(num) - 1
        while i < j:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
        return True


s = Solution()
print(s.isPalindrome(12321))
print(s.isPalindrome(1231))
print(s.isPalindrome(11211))
