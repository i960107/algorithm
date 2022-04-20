from typing import List, Set
from collections import defaultdict


def solution_fail(n: int, prerequisites: List[List[int]]) -> bool:
    d = defaultdict(list)
    # prerequisites에 명시되어있지 않으면 가능
    for c1, c2 in prerequisites:
        d[c1].append(c2)

    def dfs(i, path: List[int]):
        if len(path) == n:
            return True
        # prerequisite 다 수강했는지 확인
        if d[i]:
            for pre in d[i]:
                if pre not in path:
                    return False
        # 다음으로 뭘 들어야하지?
        for j in range(n):
            if j not in path:
                dfs(j, path + [i])

    for i in range(n):
        if dfs(i, []):
            return True

    return False


def solution(n: int, prerequisites: List[List[int]]) -> bool:
    '''DFS로 순환 구조 판별'''
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    # 이미 방문했던 노드를 저장. 중복 방문하게 된다면 순환 구조임.
    traced = set()

    def dfs(i):
        # 순환 구조이면 false?
        if i in traced:
            return False
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 탐색. 그렇지 않으면 형제 노드가 방문한 노드까지 남게 됨
        traced.remove(i)

        return True

    # n개의 코스내 모든 순열에 대해서 prerequisite 만족하면서 전체 과목 수강가능하지 확인 X
    # prerequisite이 순환 형태인지 확인
    # dictionary changed size during iteration. graph를 defaultdict에서 분리해서 고정시킬 필요가 있다. 새로운 복사본을 만듬.
    for x in list(graph):
        if not dfs(x):
            return False

    return True


def solution2(n: int, prerequisites: List[List[int]]) -> bool:
    '''가지치기를 이용한 최적화'''
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    # 이미 방문했던 노드를 저장. 중복 방문하게 된다면 순환 구조임.
    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 false?
        if i in traced:
            return False
        # 이미 방문했던 노드이면 True
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 탐색. 그렇지 않으면 형제 노드가 방문한 노드까지 남게 됨
        traced.remove(i)
        visited.remove(i)

        return True

    # n개의 코스내 모든 순열에 대해서 prerequisite 만족하면서 전체 과목 수강가능하지 확인 X
    # prerequisite이 순환 형태인지 확인
    for x in list(graph):
        if not dfs(x):
            return False

    return True


def solution_test(n: int, prerequisites: List[List[int]]) -> bool:
    # 순환 구조만 아니면 가능!
    d = defaultdict(list)

    for a, b in prerequisites:
        d[a].append(b)

    def dfs(c: int, visited: Set) -> bool:
        # n은 언제 쓰이지?

        # 언제 순환 참조 확인이 끝났다고 할 수 있지?
        # if len(visited) == len(d): return True

        if c in visited:
            return False

        visited.add(c)

        for c2 in d[c]:
            result = dfs(c2, visited)
            if not result:
                return False

        return True

    for c in list(d):
        result = dfs(c, set())
        if not result:
            return result

    return True


print(solution_test(2, [[1, 0]]))
print(solution_test(2, [[1, 0], [0, 1]]))

print(solution(2, [[1, 0]]))
print(solution(2, [[1, 0], [0, 1]]))
