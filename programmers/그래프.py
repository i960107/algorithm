from typing import Dict, List
from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}


def test_bfs(graph: dict, start_value: int) -> List[int]:
    answer = []
    queue = [start_value]
    while queue:
        v = queue.pop(0)
        if v in answer:
            continue
        answer.append(v)
        for w in graph[v]:
            queue.append(w)
    return answer


print("테스트", test_bfs(graph, 1))


def recursive_dfs(v: int, discovered=None) -> List[int]:
    '''재귀를 이용한 DFS'''
    # v로 시작하는 위치를 정해주어야함! 그래프는 따로 시작 위치 없음?
    # 아님! 어디서 시작하는지에 따라서 탐색할 수 있는 범위 달라짐. 연결된 곳만 탐색 가능. 방향이 있기 때문에!
    if discovered is None:
        discovered = []
    discovered.append(v)
    for w in graph[v]:
        # w in discovered 이미 방문한 노드인 경우 재귀 호출 종료
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


print(recursive_dfs(1))
print(recursive_dfs(7))


def iterative_dfs(v: int) -> List[int]:
    '''스택을 이용한 DFS'''
    discovered = []
    stack = [v]
    while stack:
        # 가장 마지막에 삽입된 노드부터 꺼내서 반복하게 되므로 recursive_dfs랑 방문 순서는 다르지만
        # dfs임. sibling 사이에는 순서 없음!
        w = stack.pop()
        if w not in discovered:
            discovered.append(w)
            for adjacent in graph[w]:
                stack.append(adjacent)
    return discovered


print(iterative_dfs(1))
print(iterative_dfs(7))


def bfs(v: int) -> List[int]:
    '''큐를 이용한 BFS(재귀로는 구현 불가)'''
    discovered = []
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                queue.append(w)
    return discovered


print(bfs(1))
