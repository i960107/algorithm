from typing import List
from collections import defaultdict, Counter


class Solution:
    def minWindow_fail(self, s: str, t: str) -> str:
        # 그냥 문자별 갯수를 세면 매번 모든 문자에 대해서 부족한 문자 있는지 체크해야함.
        # missing(부족한 unique character 혹은 부족한 chratcter?)을 보조로 사용해서 부족한 문자의 개수?를 체크하면 좋음
        required = defaultdict(int)
        missing = 0
        for c in t:
            required[c] += 1
            missing += 1

        # 마지막 값 반환위해서 minimum window의 left, right 기억해두어야함.
        left, right = 0, len(s)
        l = 0
        for r in range(len(s)):
            if s[r] in required:
                required[s[r]] -= 1
                # 필요한 문자였다면
                if required[s[r]] >= 0:
                    missing -= 1

            # 왼쪽 포인터 오른쪽으로 이동시킬 수 있는지 체크.
            while s[l] not in required or required[s[l]] < 0:
                # 중요! 이 체크를  while문 안에서 해야함.? < 0
                if r - l + 1 < right - left + 1:
                    left, right = l, r
                # defaultdict일 경우 s[l] in requried는 키가 안 생기지만
                # required[s[l]] >= 1하면 키가 생김
                if s[l] in required:
                    required[s[l]] += 1
                    if required[s[l]] >= 1:
                        missing += 1
                l += 1

        return s[l:r + 1] if right - left + 1 <= len(s) else ""

    def minWindow(self, s: str, t: str) -> str:

        # len(s) <= len(t)
        l = 0
        # 필요하지 않은 글자라도 deafultdict로 item만들어두는 것이 편할듯
        required = defaultdict(int)
        for c in t:
            required[c] += 1
        missing = len(t)

        start, end = 0, len(s)
        # string index out of range 예외 어쩔건데...
        for r in range(len(s)):
            required[s[r]] -= 1
            # 잘못됨
            # if required[s[r]] == 0:
            #     missing -= 1
            if required[s[r]] >= 0:
                missing -= 1

            # 한번 조건을 만족하고 나면 그 이후에는 그보다 작은 window만 고려한다.
            # while문 안에서 해야하나? -> 조건을 만족할때만 substring일때만 값 갱신해야하므로 While문 안에서만.
            # 하지만 while문안에서는 매번 길이가 줄어들기만 하므로 마지막에 한번만 체크하면됨.
            while missing == 0 and required[s[l]] < 0:
                required[s[l]] += 1
                # if required[s[l]] == 1:
                l += 1
            if missing == 0 and r - l < end - start:
                start, end = l, r
            print(l, r, missing)

        return s[start: end + 1] if end != len(s) else ""

    # 왜 missing만 기록하면 안되나. 현재 a가 잉여의 a인지, 필수 a인지 missing만 가지고는 알 수 없고,
    # required["a"] < 0이면 잉여의 a지만 다른 dict items들을 살펴봐야 전체 글자들을 다 포함하는지 판단할 수 있다.
    def minWindow2(self, s: str, t: str) -> str:
        missing = len(t)
        required = defaultdict(int)
        for c in t:
            required[c] += 1

        l = 0
        start, end = 0, len(s)

        # l,r inclusive. 처음(r=0)만 l = r이며 그 이후에는 항상 l < r이 됨.
        for r in range(len(s)):
            if required[s[r]] > 0:
                missing -= 1
            required[s[r]] -= 1

            while missing == 0 and required[s[l]] < 0:
                # 항상 required[s[l]] < 0이므로 필수적인 숫자일리가 없다.
                required[s[l]] += 1
                l += 1
            if missing == 0 and r - l < end - start:
                start, end = l, r
        return s[start:end + 1] if end != len(s) else ""

    def minWindow3(self, s: str, t: str) -> str:
        required = Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, char in enumerate(s, 1):
            missing -= (required[char] > 0)
            required[char] -= 1

            # missing == 0인 것을 한번만 체크하면 됨
            # 왜냐하면 required[s[left]] < 0인 경우에만 left pointer를 움직이기 때문에
            # missing이 다시 증가하는 경우 없음
            if missing != 0:
                continue

            while required[s[left]] < 0:
                required[s[left]] += 1
                left += 1

            if not end or right - left < end - start:
                start, end = left, right

            # 한번 조건을 만족하는 window를 찾았다면 최소 window보다 더 작으면서 조건을 만족하지 않는 window에서 다시 시작
            required[s[left]] += 1
            missing += 1
            left += 1
        return s[start:end]


s = Solution()
print(s.minWindow2(s="ADOBECODEBANC", t="ABC"))
print(s.minWindow2(s="a", t="a"))
print(s.minWindow2(s="a", t="aa"))
print(s.minWindow2(s="aa", t="aa"))
