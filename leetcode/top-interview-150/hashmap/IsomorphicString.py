from typing import List


class Solution:
    # WordPattern과 같음. 다만 하나의 문자열의 대상으로 각 문자가 패턴 요소가 됨.
    # s와 t가 길이가 다른 경우는 없음.
    # 둘다 아스키 문자로만 이루어져있음(특수문자, 숫자일 수 있음)
    # 빈 문자열일 수 없음
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        occurred = set()
        for p, c in zip(s, t):
            # 이미 문자가 할당된 상태라면
            if (c in d and d[c] != p) or (c not in d and p in occurred):
                return False
            occurred.add(p)
            d[c] = p
        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
