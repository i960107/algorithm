from typing import List
from collections import Counter


class Solution:
    # magazine의 단어를 사용해서 ransomNote를 만들 수 있는가
    # magazine의 한번 사용된 단어를 다시 사용할 수 없다.
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        chars = Counter(magazine)

        for c in ransomNote:
            if c not in chars or chars[c] <= 0:
                return False
            chars[c] -= 1
        return True

    # Counter의 합집합 연산 사용 -> 더 빠름
    # 글자를 하나하나 세는게 아니라서 중복된 문자들을 한번에 처리해서?
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        magazineChars = Counter(magazine)
        ransomNoteChars = Counter(ransomNote)

        return magazineChars & ransomNoteChars == ransomNoteChars


s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))

a = [1, 2]
b = [1, 2]
print(id(a))
print(id(b))
print(a == b)
