from typing import List


class Solution:
    # sorted일 경우에만 유효
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        left, right = 0, 0
        result = []
        while left < len(intervals):
            end = intervals[right][1]
            while right + 1 < len(intervals) and intervals[right + 1][0] <= end:
                right += 1
                if intervals[right][1] > end:
                    end = intervals[right][1]
            result.append([intervals[left][0], end])
            left = right + 1
            right = left
        return result


s = Solution()
print(s.merge(intervals=[[1, 3], [2, 6], [6, 8], [8, 10], [15, 18]]))
print(s.merge([[1, 4], [0, 4]]))
print(s.merge([[1, 4], [0, 5]]))
print(s.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
