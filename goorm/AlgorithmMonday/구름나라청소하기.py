from sys import stdin, setrecursionlimit
from collections import defaultdict
from typing import List, Dict


def solution(n: int, k: int, adj: Dict[int, List[int]], trash: List[int]) -> int:
    answer = 0

    def _dfs(city: int, accumulated_trash: int, visited: List[bool]):
        if visited[city] or accumulated_trash == k:
            nonlocal answer
            answer = max(answer, accumulated_trash)
            return

        visited[city] = True
        # 치우지 않고 경우
        for next in adj[city]:
            _dfs(next, accumulated_trash, visited.copy())

        accumulated_trash += trash[city]

        if accumulated_trash > k:
            return

        # 치우고 가는 경우
        for next in adj[city]:
            _dfs(next, accumulated_trash, visited.copy())

    _dfs(1, 0, [False] * (n + 1))
    return answer


n, k = map(int, input().split())
read = stdin.readline

adj = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, read().split())
    adj[u].append(v)
    adj[v].append(u)

trash = [0] + list(map(int, read().split()))
setrecursionlimit(10 ** 8)

print(solution(n, k, adj, trash))
