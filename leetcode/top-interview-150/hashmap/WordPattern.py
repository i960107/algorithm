from typing import List


class Solution:
    # 단어들로 이루어진 문자열 s가 pattern을 따르는지 확인하는 문제
    # 단어: 단어를 의미하는 문자열
    # 문자열은 비어있을 수 없다.
    # any trailing or leading spaces 없고, 단어를 사이에만 공백이 존재 -> split()으로 나눌 수 있다
    # 같은 문자를 다른 p로 표현하거나 다른 문자를 같은 p로 표현하면 에러임.
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        d = dict()
        characters = set()
        # 문자가 나타내는 p도 알아야하고 p 중복되지 않아야함.

        if len(words) != len(pattern):
            return False

        for p, word in zip(pattern, words):
            if (word in d and d[word] != p) or (word not in d and p in characters):
                return False
            else:
                d[word] = p
                characters.add(p)
        return True


s = Solution()
print(s.wordPattern(pattern="abba", s="dog cat cat dog"))
print(s.wordPattern(pattern="abba", s="dog cat cat fish"))
print(s.wordPattern(pattern="aaa", s="a a a a"))
