from typing import List


# 왜 category가 math
class Solution:
    # palindrome 넘버는 항상 % 11 = 0? 아님 313
    def isPalindrome(self, x: int) -> bool:
        # print(str(x)) # x가 음수일 경우 -x
        # if x < 0:
        #     return False
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-i - 1]:
                return False
        return True

    # 문자열 변환 없이
    # reverse only half of the digits
    def isPalindrome2(self, x: int) -> bool:
        # 음수이거나 0으로 끝나는 경우
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x = x // 10
        print(x, half)
        return x == half or x == half // 10


s = Solution()
print(s.isPalindrome2(121))
print(s.isPalindrome2(-121))
print(s.isPalindrome2(10))
print(s.isPalindrome2(1))
print(s.isPalindrome2(1234321))
print(s.isPalindrome2(313))
