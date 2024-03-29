from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for later, first in prerequisites:
            graph[first].append(later)
            indegree[later] += 1

        answer = []
        stack = [i for i, d in enumerate(indegree) if d == 0]
        while stack:
            curr = stack.pop()
            answer.append(curr)
            for nxt in graph[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    stack.append(nxt)
        return answer if len(answer) == numCourses else []


s = Solution()
print(s.findOrder(2, [[1, 0]]))
print(s.findOrder(2, [[1, 0], [0, 1]]))
