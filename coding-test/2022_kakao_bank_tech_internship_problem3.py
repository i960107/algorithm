from typing import List, Dict, Set
from collections import defaultdict


def solution(rooms: List[int]):
    adj = defaultdict(list)
    for i, key in enumerate(rooms):
        adj[i + 1].append(key)

    paths = get_consecutive_paths(adj)

    return max(len(paths) - 1, 1)


def get_consecutive_paths(adj: Dict[int, List[int]]) -> List[Set[int]]:
    visited = set()

    def _get_path(start: int) -> Set[int]:
        path = set()

        curr = start
        # visited.add(curr)

        while True:
            next = adj[curr][0]
            if next in path:
                break
            path.add(next)
            curr = next

        visited.update(path)
        return path

    paths = []
    for start_room in adj.keys():
        if start_room in visited:
            continue
        paths.append(_get_path(start_room))

    return paths


print(solution([3, 1, 2, 4]))
print(solution([2, 3, 4, 5, 1]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([2, 3, 1, 5, 6, 4, 7, 6]))
