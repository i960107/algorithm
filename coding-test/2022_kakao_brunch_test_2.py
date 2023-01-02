from typing import List


def solution_temp(cost: List[int], x: int) -> int:
    n = len(cost)

    max_profit = 0

    def dfs(node: int, path: List[int], cost_accumulated: int):

        if node >= n or cost_accumulated + cost[node] >= x:
            nonlocal max_profit
            profit = 0
            if node < n and cost_accumulated + cost[node] == x:
                path.append(node)
                cost_accumulated += cost[node]
            for visited_node in path:
                profit += (2 ** visited_node)
            max_profit = max(max_profit, profit)
            print(path, cost_accumulated, profit)
            return

        path += [node]
        cost_accumulated += cost[node]

        for next in range(node + 1, n + 1):
            dfs(next, path.copy(), cost_accumulated)

    for node in range(n):
        dfs(node, [], 0)
    return max_profit % (10 ** 9 + 7)


class Node:
    def __init__(self, index: int, cost: int):
        self.profit = 2 ** index
        self.index = index
        self.cost = cost

    def __lt__(self, other):
        if self.cost <= other.cost:
            return True
        return False


def solution(cost: List[int], x: int) -> int:
    if sum(cost) < x:
        return sum([2 ** i for i in range(len(cost))]) % (10 ** 9 + 7)

    n = len(cost)
    max_profit = 0
    sorted_cost = [Node(i, c) for i, c in enumerate(cost)]
    sorted_cost.sort(reverse=True)
    print([node.cost for node in sorted_cost])
    visited = [False] * n

    def dfs(sorted_index: int, profit_accumulated: int, cost_accumulated: int, path: List[int]):
        node = None
        if sorted_index < n:
            node = sorted_cost[sorted_index]

        if not node or node.index >= n or cost_accumulated + node.cost >= x:
            nonlocal max_profit
            if node and node.index < n and cost_accumulated + node.cost == x:
                profit_accumulated += node.profit
                cost_accumulated += node.cost
                path.append(node.index)
            if profit_accumulated > max_profit:
                max_profit = profit_accumulated
                for node in path:
                    visited[node] = True
            return

        profit_accumulated += node.profit
        cost_accumulated += node.cost
        path += [node.index]

        for next in range(sorted_index + 1, n + 1):
            dfs(next, profit_accumulated, cost_accumulated, path.copy())

    for i in range(n):
        if visited[i]:
            continue
        dfs(i, 0, 0, [])
    return max_profit % (10 ** 9 + 7)


print(solution([3, 4, 1], 8))  # case0  7
print(solution_temp([19, 78, 27, 18, 20], 25))  # case1 expected 16
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55))  # case2
print(solution([100], 1000))  # case3
# print(solution([2, 5, 6, 25, 22, 21, 7, 9, 7, 22], 95))  # case4
# print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 648903036))  # case11
