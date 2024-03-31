from typing import List
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        INF = 'INF'

        d = defaultdict(set)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x2 - x1 == 0:
                    d[(INF, x1)].add((x1, y1))
                    d[(INF, x1)].add((x2, y2))
                    continue

                incl = (y2 - y1) / (x2 - x1)
                yintercep = y1 - incl * x1
                # print(x1, y1, x2, y2,"기울기", incl, "y절편", yintercep)
                d[(incl, yintercep)].add((x1, y1))
                d[(incl, yintercep)].add((x2, y2))

        max_key = max(d, key=lambda key: len(d[key]))
        return len(d[max_key])


s = Solution()
print(s.maxPoints(points=[[1, 1], [2, 2], [3, 3]]))
print(s.maxPoints(points=[[1, 1], [1, 2], [1, 3]]))
print(s.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
