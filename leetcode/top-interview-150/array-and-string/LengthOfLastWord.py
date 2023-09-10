from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tokens = s.split()
        return len(tokens[-1])

    # 앞과 뒤에 공백이 여러개 올 수 있다.
    def lengthOfLastWord2(self, s: str) -> int:
        l = 0
        last_len = 0
        for c in s:
            if c.isalpha():
                l += 1
            else:
                if l:
                    last_len = l
                l = 0
        if l:
            last_len = l
        return last_len


s = Solution()
print(s.lengthOfLastWord2(s="Hello World"))
# 한단어인 경우
print(s.lengthOfLastWord2(s="abc"))
print(s.lengthOfLastWord2(s="abc c "))
print(s.lengthOfLastWord2(s="   fly me   to   the moon  "))
