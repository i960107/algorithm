from typing import List
from collections import defaultdict


def solution(tickets: List[List[str]]) -> List[str]:
    n = len(tickets)

    graph = defaultdict(list)
    for i, (src, dest) in enumerate(tickets):
        graph[src].append((dest, i))

    for src, dests in graph.items():
        graph[src] = sorted(dests)

    # 같은 경로의 항공권이 있을 수 있나? -> 없다.
    def dfs(src: str):
        nonlocal answer
        if len(used) == n and not answer:
            answer = path[::]
            return

        for nxt, i in graph[src]:
            if i in used:
                continue
            used.add(i)
            path.append(nxt)
            dfs(nxt)
            path.pop()
            used.remove(i)

    START = "ICN"
    path = [START]
    # 사용한 티켓의 인덱스
    used = set()

    answer = None
    dfs(START)

    return answer


# print(s.solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
