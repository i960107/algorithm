import heapq
from collections import deque
from typing import List, Tuple, Dict


# dp랑 무슨 관련이 있지?
class Solution:
    def coinChangeFail(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        count = 0
        for coin in coins:
            coinCount = amount // coin
            count += coinCount
            amount -= (coinCount * coin)
        return count if amount == 0 else -1

    # 다익스트라 -> amount에 비해 coin이 너무 작을 경우 MLE
    # 이미 쓴 동전 쓰지 말기
    def coinChangeFail2(self, coins: List[int], amount: int) -> int:
        coins.sort()
        queue = []
        queue.append((0, 0, 0))
        visited = set()
        # heapq는 minheap
        while queue:
            count, curr, i = heapq.heappop(queue)

            if curr == amount:
                return count

            if curr > amount:
                continue

            visited.add(curr)

            for j in range(i, len(coins)):
                coin = coins[j]
                for coin_count in range(1, (amount - curr) // coin + 1):
                    nxt_count, nxt = count + coin_count, curr + coin_count * coin
                    # 여기서 체크하면 안됨 -> 1 * 11개 들어가고 visited 체크되어서 11이 안들어감.
                    # coins.sort(reverse=True)로 코인 갯수 적은 것부터 삽입되도록..
                    # 여기서 바로 반환하면 안됨.. 최소값이라고 보장할 수 없음.
                    if nxt in visited:
                        continue
                    if nxt > amount:
                        break
                    heapq.heappush(queue, (nxt_count, nxt, j + 1))
        return - 1

    # dfs(basically brute force) -> 중복된 하위 문제 제거
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c < 0:
                    continue
                if dp[a] > dp[a - c] + 1:
                    dp[a] = dp[a - c] + 1
        return dp[amount] if dp[amount] != INF else -1


s = Solution()
print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([1, 2, 5], 100))
print(s.coinChange([2], 3))
print(s.coinChange([3], 2))
print(s.coinChange([1], 0))
# dp인 이유
# kanpsack problem이 greedy vs dp
print(s.coinChange([2, 3], 7))


# 다익스트라: x-> 각 노드까지 가는 최단 거리 찾기.
# bfs + heapq
# 우선순위 큐를 사용하기 때문에 이미 값이 있다면 현재 값은 최단 경로가 될 수 없다. 한번만 업데이트 한다.
def dijkstra(graph: Dict[int, Tuple[int, int]]):
    INF = float('INF')
    distances = [INF for _ in range(len(graph))]
    # distance, node
    queue = [(0, 0)]

    # 넣을때 체크 x 넣을때는 최소값 보장할 수 없음.-> 빼면서 체크...

    while queue:
        distance, curr = heapq.heappop(queue)
        if distances[curr] != INF:
            continue
        distances[curr] = distance
        for dist, nxt in graph[curr]:
            heapq.heappush(queue, (distance + dist, nxt))
