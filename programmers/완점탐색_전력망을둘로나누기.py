from typing import List, Dict
from collections import defaultdict


# 트리를 둘로 나누기.
def solution(n: int, wires: List[List[int]]) -> int:
    adj = defaultdict(list)
    for u, v in wires:
        adj[u].append(v)
        adj[v].append(u)

    answer = n
    for u, v in wires:
        result = divide(n, adj, u, v)
        if result != -1 and result < answer:
            answer = result
    return answer


# 나눠진 것의 트리가 2개여야함.
# u와 v에서 시작한 각각의 그래프.
# 나눠진 트리가 2개 초과라면 -1,나눠진 트리가 2개라면 두 트리 사이의 개수의 차이를 반환
def divide(n: int, adj: Dict[int, List], u: int, v: int) -> int:
    u_tree = []
    u_stack = [u]
    visited = [False] * (n + 1)
    while u_stack:
        now = u_stack.pop()
        visited[now] = True
        u_tree.append(now)
        for nxt in adj[now]:
            # 먼저 visited처리 해주어도됨.
            if visited[nxt] or (now == u and nxt == v):
                continue
            u_stack.append(nxt)

    v_tree = []
    v_stack = [v]
    while v_stack:
        now = v_stack.pop()
        visited[now] = True
        v_tree.append(now)
        for nxt in adj[now]:
            if visited[nxt] or (now == v and nxt == u):
                continue
            v_stack.append(nxt)

    if len(u_tree) + len(v_tree) != n:
        return -1
    return abs(len(u_tree) - len(v_tree))


def dfs(adj: Dict[int, List[int]], u: int, visited: List[bool]) -> int:
    visited[u] = True
    return sum([1] + [dfs(adj, nxt, visited) for nxt in adj[u] if not visited[u]])

    # 이미 한개의 그래프이기 때문에 하나의 간선을 제거하면 두개의 트리가 됨


def solution2(n: int, wires: List[List[int]]) -> int:
    adj = defaultdict(list)
    for u, v in wires:
        adj[u].append(v)
        adj[v].append(u)

    answer = n
    for u, v in wires:
        visited = [False] * (n + 1)
        visited[u] = True
        visited[v] = True
        result = (dfs(adj, u, visited) - dfs(adj, v, visited))
        if result < answer:
            answer = result

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
