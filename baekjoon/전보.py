from sys import stdin

from collections import defaultdict
import heapq

INF = int(1e9)
read = stdin.readline
N, M, C = map(int, input().split())
adj = defaultdict(list)
for _ in range(M):
    a, b, cost = map(int, read().split())
    adj[a].append((b, cost))

queue = []
queue.append((0, C))
distance = [INF] * (N + 1)

while queue:
    acc_dist, curr = heapq.heappop(queue)
    if distance[curr] != INF:
        continue
    distance[curr] = acc_dist
    for next, dist in adj[curr]:
        next_dist = acc_dist + dist
        if distance[next] <= next_dist:
            continue
        distance[next] = next_dist
        heapq.heappush(queue, (next_dist, next))

count = sum(1 for distance in distance if distance != INF) - 1
total_distance = max(distance for distance in distance if distance != INF)
print(count, total_distance)
