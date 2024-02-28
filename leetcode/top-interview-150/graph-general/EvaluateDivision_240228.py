from typing import List, Dict
from collections import defaultdict, deque


class Solution:
    # 길이가 2일때 equqation 두개를 합쳐서 결과를 낼 수 있는 경우는 없나?
    # ab/cd를 구해야하고 a/c b/d가 주어져있을때?
    # a/b, bc/cd가 주어져있고, ab/cd를 구해야할때?
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def buildGraph(equations: List[List[str]], values: List[float]) -> Dict:
            graph = dict()
            for (a, b), value in zip(equations, values):
                if a not in graph:
                    graph[a] = dict()
                graph[a][b] = value

                if b not in graph:
                    graph[b] = dict()
                graph[b][a] = 1.0 / value
            return graph

        # 이미 방문한 경로는 방문하지 말기.
        # 경로 하나를 찾아야함.
        def dfs(src: int, dest: int):
            if src in visited:
                return -1.0
            visited.add(src)
            for nxt in graph[src]:
                if nxt == dest:
                    return graph[src][nxt]
                result = dfs(nxt, dest)
                if result != -1:
                    print(nxt)
                    return graph[src][nxt] * result
            return -1.0

        graph = buildGraph(equations, values)
        answer = []
        for dividend, divisor in queries:
            # dividend, divisor가 한번이라도 equations에 등장했는지 체크 아니면 undefined
            if dividend not in graph or divisor not in graph:
                answer.append(-1.0)
                continue

            if dividend == divisor:
                answer.append(1.0)
                continue

            visited = set()
            answer.append(dfs(dividend, divisor))
        return answer

    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for (a, b), value in zip(equations, values):
            adj[a].append((b, value))
            adj[b].append((a, value))

        # 왜 dfs가 아니라, bfs를 사용할까?

        def bfs(src, target) -> float:
            if src not in adj or target not in adj:
                return -1.0
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append([nei, w * weight])

            return -1

        return [bfs(q[0], q[1]) for q in queries]


s = Solution()
# print(s.calcEquation2(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
#                       queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))
#
# print(s.calcEquation(equations=[["a", "b"]], values=[0.5], queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))
# 이건 구할 수 있지 않나?
print(s.calcEquation(equations=[["a", "b"], ["ac", "cd"]], values=[0.5, 2], queries=[["a", "d"]]))
