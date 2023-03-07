from collections import defaultdict
import heapq

INF = int(1e9)
N, M = map(int, input().split())
adj = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# A -> K -> X
# 다익스트라 2번 vs 플루이드 워셜
# 둘다 가능하지만 2NLogN vs N^3
X, K = map(int, input().split())


# 도달할 수 없는 경우 있는지 주의!!
def get_shortest_path(start: int, end: int) -> int:
    distance = [INF] * (N + 1)

    queue = []
    queue.append((0, start))

    while queue:
        acc_dist, curr = heapq.heappop(queue)

        if distance[curr] < acc_dist:
            continue

        distance[curr] = acc_dist

        if curr == end:
            break

        for next in adj[curr]:
            cost = acc_dist + 1
            heapq.heappush(queue, (cost, next))

    return distance[end]


res1 = get_shortest_path(1, K)
res2 = get_shortest_path(K, X)
if res1 == INF or res2 == INF:
    print(-1)
else:
    print(res1 + res2)
