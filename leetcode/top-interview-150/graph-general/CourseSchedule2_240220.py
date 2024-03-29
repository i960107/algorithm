from typing import List
from collections import defaultdict, deque


class Solution:
    # undefined : many path
    # unique path:
    # impossible : cyclic
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        answer = []
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for object, pre in prerequisites:
            graph[pre].append(object)
            indegree[object] += 1

        queue = deque()
        for object in range(numCourses):
            if indegree[object] == 0:
                queue.append(object)

        while queue:
            object = queue.popleft()
            answer.append(object)

            for nxt in graph[object]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return answer if len(answer) == numCourses else []



s = Solution()
print(s.findOrder(numCourses=2, prerequisites=[[1, 0]]))
print(s.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
print(s.findOrder(numCourses=4, prerequisites=[[1, 0], [0, 1], [3, 1], [3, 2]]))
