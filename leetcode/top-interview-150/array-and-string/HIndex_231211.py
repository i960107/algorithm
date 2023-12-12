from typing import List


class Solution:
    def hIndex(self, citations: List[int]):
        citations.sort(reverse=True)
        hIndex = 0
        for i in range(len(citations)):
            # 둘 중의 작은 값?
            citation, count = citations[i], i + 1
            if citation < count:
                break
            hIndex = count
        return hIndex

    # 정렬된 배열 -> parametric search 생각할 수 있어야...
    def hIndex2(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        lo, hi = 0, len(citations) - 1
        hIndex = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            # 더 큰 값으로 갱신해갈때는 papers 기준으로
            if citations[mid] < mid + 1:
                hIndex = mid + 1
                lo = mid + 1
            else:
                hi = mid - 1
        return hIndex

    def hIndex3(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        lo, hi = 0, n - 1
        hIndex = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            p, c = n - mid, citations[mid]
            print(mid, p, c)
            if c < p:
                lo = mid + 1
            else:
                hIndex = p
                hi = mid - 1
        return hIndex


s = Solution()
# [0,1,2,5,6], [0,1,3,5,6]
print(s.hIndex3([3, 0, 6, 1, 5]))
print(s.hIndex3([1, 3, 1]))
print(s.hIndex3([0, 0, 0]))
print(s.hIndex3([2, 2]))
