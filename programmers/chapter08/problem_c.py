from typing import Final, List, Dict
from collections import defaultdict


def get_longest_path_length(origin: int, dest: int, adj: Dict[int, List[int]]) -> int:
    visited = [False] * (len(adj) + 1)

    # 경로가 없는 경우
    NO_PATH: Final = -100

    def _get_longest_path_length(current: int, goal: int) -> int:

        # 이미 방문한 노드라면 경로를 만들 수 없다
        # 경로가 없는 경우 길이를 음수로 표현하자
        if visited[current]:
            return NO_PATH

        # 목적지라면 0부터 역으로 길이를 가산해나가자
        elif current == goal:
            return 0

        visited[current] = True

        max_length = NO_PATH

        for next in adj[current]:
            max_length = max(max_length, _get_longest_path_length(next, goal) + 1)

        visited[current] = False
        return max_length

    return _get_longest_path_length(origin, dest)


n, m = map(int, input().split())
adj = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

origin, dest = map(int, input().split())
answer = get_longest_path_length(origin, dest, adj)

print(answer if answer else 0)
