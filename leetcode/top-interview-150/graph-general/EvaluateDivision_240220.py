from typing import List, Dict
from collections import defaultdict


class SolutionFail:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 직접 이어져 있지 않아도 cache에 추가되어있을 수 있음.
        # -1인 경우는 추가해두지 않음.
        cache = dict()
        graph = defaultdict(list)
        # 양방향으로 연결해두면 infinite recursion error발생.
        for (x, y), value in zip(equations, values):
            graph[x] = y
            cache[(x, y)] = value
            graph[y] = x
            cache[(y, x)] = 1 / value

        # 순환이 있을 수 있나
        # 매 단계마다 캐싱을 해야하나

        def getResult(x: str, y: str) -> float:
            print(x, y)
            if x in visited:
                return -1

            if x not in graph:
                return -1

            if x == y:
                return 1

            # if nxt in graph[x] 와 같음.
            if (x, y) in cache:
                return cache[(x, y)]

            visited.append(x)

            for nxt in graph[x]:
                res = getResult(nxt, y)
                if res == -1:
                    continue
                cache[(x, y)] = cache[(x, nxt)] * res
                break
            visited.pop()

            return cache[(x, y)] if (x, y) in cache else -1

        visited = []
        answer = []

        for x, y in queries:
            if len(x) == 1:
                answer.append(getResult(x, y))
                continue
            # 길이가 2일때 어떻게 처리하는게 가장 이상적일까?
            res1 = getResult(x[0], y[1])
            res2 = getResult(x[1], y[0])
            if res1 != -1 and res2 != -1:
                answer.append(res1 * res2)
                print("First", res1, res2)
                continue
            res1 = getResult(x[0], y[0])
            res2 = getResult(x[1], y[1])
            answer.append(res1 * res2)
            print("second", res1, res2)
        return answer


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildGraph(equations, values)
        answer = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                answer.append(-1.0)
                continue
            visited = set()
            result = [-1]
            temp = 1.0
            self.dfs(dividend, divisor, graph, visited, result, temp)
            answer.append(result[0])
        return answer

    # 양방향 그래프 생성
    def buildGraph(self, equations: List[List[str]], values: List[float]) -> Dict:
        # 2차원 그래프?  dict의 value도 dict
        graph = dict()

        for (dividend, divisor), value in zip(equations, values):
            if dividend not in graph:
                graph[dividend] = defaultdict(float)
            if divisor not in graph:
                graph[divisor] = defaultdict(float)
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value

        return graph

    def dfs(self, node, dest, graph, visited, result, temp):
        if node in visited:
            return
        visited.add(node)

        if node == dest:
            result[0] = temp
            return

        for nxt, val in graph[node].items():
            self.dfs(nxt, dest, graph, visited, result, temp * val)


s = Solution()
print(s.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                     queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
print(s.calcEquation(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
                     queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))
