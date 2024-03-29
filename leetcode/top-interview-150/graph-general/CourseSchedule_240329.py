from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for later, first in prerequisites:
            graph[first].append(later)
            indegree[later] += 1

        stack = [i for i, d in enumerate(indegree) if d == 0]
        answer = []
        count = 0

        while stack:
            count += 1
            curr = stack.pop()
            answer.append(curr)
            for nxt in graph[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    stack.append(nxt)
        return count == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # 어떤 방향으로 연결하든 순서만 뒤집힐 뿐 괜찮음.
        for x, y in prerequisites:
            graph[x].append(y)

        visited = set()
        traced = set()

        def dfs(i) -> bool:
            if i in traced:
                return False
            # 한번 방문한 경로(visited)는 방문하지 않아도됨.
            # 한 path에 대해서 중복 방문(traced)이 일어나면 -> 순환이 있다는 것으로
            if i in visited:
                return True
            traced.add(i)

            for nxt in graph[i]:
                if not dfs(nxt):
                    return False
            traced.remove(i)
            visited.add(i)
            return True

        # graph에 있는 것에 대해서만 방문해도 되나? 모든 코스들 dfs해야 하는 것 아닌가?
        # 선수 과목들 사이에 싸이클이 있는지만 판단하면 됨.
        for x in list(graph):
            if not dfs(x):
                return False
        return True


s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))
