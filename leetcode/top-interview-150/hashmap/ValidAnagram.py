from collections import Counter


class Solution:
    # 두 문자열의 길이가 같다 NO.
    # RansomNote와의 차이점 완전히 같아야함. 포함되면 된다 -> 교집합의 결과. 완전히 같아야한다 -> 합집합의 결과
    def isAnagram(self, s: str, t: str) -> bool:
        # 왜 최적화라고 생각했는데 더 느리지..?
        # len(obj) 는 obj.__len__()을 호출함 따라서 차이가 없음.
        # 보통 __를 직접 호출하지는 않음.
        # 평균적으로 length가 같은 문자열이 많아서 오히려 더 연산이 늘어나는 결과가 생기기 때문?
        if s.__len__() != t.__len__():
            return False
        # if len(s) != len(t):
        #     return False
        sCounter = Counter(s)
        tCounter = Counter(t)
        return sCounter == tCounter

    def isAnagram2(self, s: str, t: str) -> bool:
        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            if c in d and d[c] > 0:
                d[c] -= 1
            else:
                return False
        return True

    # 이 외에도 1) 정렬한 결과가 같은지 살펴보는 방법
    # 2) dict가 아닌 알파벳을 나타내는 26길이의 배열을 만들고 각 칸에 몇번 등장하는지 기록하는 방법 등이 있다.


s = Solution()
print(s.isAnagram(s="anagram", t="nagaram"))
print(s.isAnagram2(s="anagram", t="nagaram"))
