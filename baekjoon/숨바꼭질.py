from sys import stdin
from collections import defaultdict
import heapq

INF = int(1e9)
read = stdin.readline

N, M = map(int, input().split())
adj = defaultdict(list)
for _ in range(M):
    a, b = map(int, read().split())
    adj[a].append(b)
    adj[b].append(a)

queue = []
queue.append((0, 1))
distances = [INF] * (N + 1)
distances[1] = 0

while queue:
    acc_dist, curr = heapq.heappop(queue)
    if distances[curr] < acc_dist:
        continue

    for next in adj[curr]:
        if distances[next] <= acc_dist + 1:
            continue
        distances[next] = acc_dist + 1
        heapq.heappush(queue, (acc_dist + 1, next))

hide = -1
final_distance = -INF
count = 0

print(distances)
for index in range(1, N + 1):
    distance = distances[index]
    if distance == final_distance:
        count += 1
    elif distance > final_distance:
        hide, final_distance, count = index, distance, 1
print(hide, final_distance, count)
