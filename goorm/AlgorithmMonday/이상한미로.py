from sys import stdin
from typing import Dict, List, Tuple
from collections import defaultdict, deque
import heapq


class State:
    def __init__(self, node: int, remainder: int, acc_distance: int):
        self.node = node
        self.remainder = remainder
        self.acc_distance = acc_distance


def solution(n: int, rooms: List[int], adj: Dict[int, List[Tuple[int]]]):
    bfs_queue = deque()
    bfs_queue.append(State(1, -1, 0))
    visited = [0] * (n + 1)

    while bfs_queue:
        curr = bfs_queue.popleft()

        if visited[curr.node]:
            visited[curr.node] = min(visited[curr.node], curr.acc_distance)
        else:
            visited[curr.node] = curr.acc_distance

        for next, distance in adj[curr.node]:
            if curr.remainder != -1 and next % rooms[curr.node - 1] != curr.remainder:
               continue
            bfs_queue.append(State(next, next % rooms[curr.node - 1], curr.acc_distance + distance))

            if next == n:
                break

    return visited[n] if visited[n] else - 1


read = stdin.readline
n, m = map(int, read().split())
a = [0] + list(map(int, read().split()))

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, read().split())
    adj[u].append([v, w])
    adj[v].append([u, w])

answer = - 1
d = [[10 ** 18 for _ in range(10)] for _ in range(n + 1)]
d[1][0] = 0
pq = []
heapq.heappush(pq, (d[1][0], 1, 0))
while pq:
    cd, cur, prev = heapq.heappop(pq)

    if cd > d[cur][prev]:
        continue
    if cur == n:
        answer = cd
        break
    for next, nd in adj[cur]:
        if cd + nd >= d[next][cur % a[next]]:
            continue
        if cur != 1 and prev % a[cur] != next % a[cur]:
            continue
        d[next][cur % a[next]] = cd + nd
        heapq.heappush(pq, (cd + nd, next, cur % a[next]))

print(answer)
