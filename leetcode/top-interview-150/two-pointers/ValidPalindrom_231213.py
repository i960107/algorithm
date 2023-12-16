class Solution:
    #  lowercase 로 바꾸고 removing non-alphanumeric character
    def isPalindrome(self, s: str) -> bool:
        trimmed = []
        # 문자열 조작 함수 이름 외우기.
        for c in s:
            if c.isalpha():
                trimmed.append(c.lower())
            elif c.isnumeric():
                trimmed.append(c)

        i, j = 0, len(trimmed) - 1
        while i < j:
            if trimmed[i] != trimmed[j]:
                return False
            i += 1
            j -= 1
        return True


s = Solution()
print(s.isPalindrome("race a car"))
print(s.isPalindrome(s="A man, a plan, a canal: Panama"))
print(s.isPalindrome(s="A man, a plan, a canal: Panama"))
print(s.isPalindrome(s="0P"))
