from typing import List, Set, Dict
from collections import defaultdict


def solution(n: int, results: List[List[int]]) -> int:
    answer = 0
    losers = defaultdict(set)
    winners = defaultdict(set)
    for strong, week in results:
        losers[strong].add(week)
        winners[week].add(strong)

    # dfs로 탐색한 노드의 수를 반환
    def dfs(graph: Dict, node: int, visited: Set):
        if node in visited:
            return
        visited.add(node)
        for nxt in graph[node]:
            dfs(graph, nxt, visited)

    for player in range(1, n + 1):
        visited_losers = set()
        dfs(losers, player, visited_losers)
        visited_winners = set()
        dfs(winners, player, visited_winners)
        if len(visited_losers) + len(visited_winners) - 1 == n:
            answer += 1
    return answer


# 플루이드 워셜 사용
def solution2(N: int, results: List[List[int]]) -> int:
    INF = int(1e9)
    wins = [[INF] * (N + 1) for _ in range(N + 1)]

    # 거리로 해볼까
    for i in range(1, N + 1):
        wins[i][i] = 0

    for winner, loser in results:
        # 양방향으로 설정해주면 안됨..
        wins[winner][loser] = 1
        # wins[loser][winner] = 1

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                wins[a][b] = min(wins[a][b], wins[a][k] + wins[k][b])

    for row in wins:
        print(row)

    result = 0
    for a in range(1, N + 1):
        count = 0
        for b in range(1, N + 1):
            # wins[a][b] == wins[b][a]
            if wins[a][b] != INF or wins[b][a] != INF:
                count += 1
        if count == N:
            result += 1
    return result


print(solution2(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
