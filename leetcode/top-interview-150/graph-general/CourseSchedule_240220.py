from typing import List
from collections import defaultdict, deque


class Solution:
    # topological sort(kahn's algorithm), only order not directed edges
    # use stack to keep track of all vertices in the sorted order
    # vertex is pushed to the stack bottom only when all of its adjacent vertices(prerequisites) are already in stack

    # 위상정렬아니고 detect cycle. 위상 정렬은 1) 방향 그래프 2) cycle이 없고 * 모든 vertex에 대해서 순서가 있는 경우에 사용가능은 아님!!
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for after, before in prerequisites:
            adj[before].append(after)
            indegree[after] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        # cycle이 있다면 queue가 종료된 후에 indegree가 0이 아닌 1.
        while queue:
            node = queue.popleft()
            visited += 1
            for nxt in adj[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        print(indegree)
        return numCourses == visited

    # 위상 정렬 다른 버전? 이 방법으로는 cycle있는지 판별 어떻게?
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        NOT_VISITED = -1
        VISITING = 0
        VISITED = 1
        visited = [NOT_VISITED] * numCourses
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # print(s.canFinish2(2, [[1, 0]])) # 0부터 방문하고 1 -> 0으로 방문하니 잘못된 결과가 됨.
        # def topologicalSort(node):
        #     visited[node] = True
        #     for pre in graph[node]:
        #         if visited[pre]:
        #             print(node, "이미 방문한 노드")
        #             return False
        #         if not topologicalSort(pre):
        #             return False
        #     return True

        # visited True/False가 아니라 방문 전 -1 진행중 0 방문 후 1로 표시
        def topologicalSort(node):
            # 모든 작업이 다 끝나고 True가 된다.
            # 순환이 생기면 ans가 0이 됨.
            visited[node] = VISITING
            for pre in graph[node]:
                if visited[pre] == NOT_VISITED:
                    if not topologicalSort(pre):
                        return False
                elif visited[pre] == VISITING:
                    return False
                    # visited[pre] == VISITED인데 또 방문하는 경우가 있나?

            visited[node] = VISITED
            return True

        for i in range(numCourses):
            if visited[i] == VISITED:
                continue
            if not topologicalSort(i):
                return False
        return True

    # 그래프의 순환 판별
    def canFinish3(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # 한번 방문했던 그래프는 두 번 이상 방문하지 않도록 무조건 true로 리턴 -> 가지치기.
        # 순환 구조이면 return False, 이미 방문한 노드이면 return True
        visited = set()
        traced = set()

        # 모든 경로를 탐색.
        def dfs(i):
            # 순환 구조이면 false
            if i in traced:
                return False

            if i in visited:
                return True

            # 왜 방문전에 visited 체크 하면 안되지?
            # 그게 아니라 traced가 추가되고 제거되지 않은채로 return되어서 그럼.
            traced.add(i)
            visited.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            # 형제 노드가 방문한 노드까지 남게되어, 순환이 아닌데 순환이라고 잘못 판단할 수 있다.
            # 0 -> 1 -> 2, 0 ->2
            # 한번 방문한 경로는 방문하지 않아도됨.
            # 이후 모든 경로는 방문해야함.
            # traced -> 현재 경로에 대한 방문 체크. vistied -> 전체 노드에 대한 방문체
            traced.remove(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True


s = Solution()
# print(s.canFinish(2, [[1, 0]]))
# print(s.canFinish(2, [[1, 0], [0, 1]]))
# print(s.canFinish(2, [[0, 1]]))
print(s.canFinish2(2, [[1, 0]]))
print(s.canFinish2(2, [[1, 0], [0, 1]]))
print(s.canFinish2(2, [[0, 1]]))

'''순위'''
from typing import List


# 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없음 -> 위상정렬 불가. 플루이드 워셜 알고리즘 사용.
# 거쳐가는 지점을 모두 체크해서 값을 갱신.
# 정확하게 순서를 매길 수 있는 선수의 수 -> 플로이드 워셜 알고리즘을 사용해서 다른 노드까지의 거리가
def solution(n: int, results: List[List[int]]) -> int:
    INF = int(1e9)
    WIN = True
    LOSE = False

    wins = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        wins[i][i] = 0

    for winner, loser in results:
        wins[winner][loser] = WIN

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                wins[a][b] = min(wins[a][b], wins[a][k] + wins[k][b])

    result = 0
    for a in range(1, n + 1):
        count = 0
        for b in range(1, n + 1):
            if wins[a][b] != INF or wins[b][a] != INF:
                count += 1
        if count == n:
            result += 1
    return result

# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
