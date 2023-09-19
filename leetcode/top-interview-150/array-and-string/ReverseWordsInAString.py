from typing import List


class Solution:
    # leading or trailing spaces or multiple spaces between two words.
    # returned string should on ly have a single space seperating the wrods
    # O(1) extra space. if string is mutable(python은 imputable, string 조작시 새로운 string 메모리에 저장됨)
    # 투포인터를 사용해서 Reverse 할수 있을까?
    def reverseWords(self, s: str) -> str:
        # sorted 아님.
        # 문자열 정렬한 결과를 내림차순 정렬한다는 것.
        return ' '.join(s.split()[::-1])

    def reverseWords1(self, s: str) -> str:
        tokens = s.split()
        tokens.reverse()
        return ' '.join(tokens)


s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("    hello world  "))
