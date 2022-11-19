from sys import stdin
from collections import defaultdict, deque
from typing import List, Dict, Set


def solution(n: int, m: int, cards: List[int], relations: Dict[int, List]):
    def _bfs(start: int) -> List[int]:
        visited_nodes = set()
        bfs_queue = deque()
        bfs_queue.append((start, 0))

        while bfs_queue:
            curr, depth = bfs_queue.popleft()
            if curr in visited_nodes:
                continue
            visited_nodes.add(curr)
            for next in relations[curr]:
                bfs_queue.append((next, depth + 1))
        return list(visited_nodes)

    visited = [False] * (n + 1)

    def update_visited(new_visited: List[int]):
        for i in new_visited:
            visited[i] = True

    def get_unsatisfaction_score(visited_nodes: List[int]):
        visited_nodes.sort()
        visited_nodes_cards = sorted([cards[i - 1] for i in visited_nodes])
        return sum(abs(x - y) for x, y in zip(visited_nodes_cards, visited_nodes))

    total_unsatisfaction_score = 0
    for i in range(1, n + 1):
        if not visited[i]:
            visited_nodes = _bfs(i)
            update_visited(visited_nodes)
            total_unsatisfaction_score += get_unsatisfaction_score(visited_nodes)
    return total_unsatisfaction_score


read = stdin.readline
n, m = map(int, input().split())

cards = list(map(int, input().split()))

relations = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    relations[u].append(v)
    relations[v].append(u)

print(solution(n, m, cards, relations))
