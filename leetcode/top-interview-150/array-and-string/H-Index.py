from typing import List


class Solution:
    # x 1 ~ 1000까지 인용회수가 x이상인 것의 개수 -> 정렬이 필요함
    # O(LogN * LogN)
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        # h의 범위 1 ~ citaions[-1] 최대값
        lo, hi = 0, citations[-1]
        h_index = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            # 값이 citations[mid]보다 큰 것들 중 최소값의 인덱스
            if len(citations) - self.binary_search(citations, mid) >= mid:
                h_index = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return h_index

    def binary_search(self, nums: List[int], target: int):
        lo, hi = 0, len(nums)
        result = None
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid - 1
                result = mid
            else:
                lo = mid + 1
        return result


s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))
print(s.hIndex([2, 2, 2, 2, 2]))
