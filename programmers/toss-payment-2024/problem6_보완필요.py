from typing import List, Set


def solution_fail(money: int, stocks: List[List[int]]) -> int:
    n = len(stocks)
    max_value = 0
    max_visited = set()

    stocks.sort(key=lambda x: -x[1])
    print(stocks)

    # 순서가 중요하지 않음.. -> 순열 아닌 조합
    # 0일때 어떻게 처리하는게 좋을까...
    def dfs(i: int, left_money: int, acc_value: int, visited: Set[int]):
        if left_money < stocks[i][1]:
            nonlocal max_value
            if max_value < acc_value:
                max_value = acc_value
                max_visited = visited.copy()
            print()
            return

        left_money -= stocks[i][1]
        acc_value += stocks[i][0]
        visited.add(i)

        if left_money == 0:
            nonlocal max_value, max_visited
            if max_value < acc_value:
                max_value = acc_value
                max_visited = visited.copy()

        for nxt in range(i + 1, n):
            nonlocal max_visited
            # 이미 max_visited에 포함되어있으면 최대 profit 얻을 수 없음
            if nxt in max_visited:
                continue
            dfs(nxt, left_money, acc_value, visited)

        visited.remove(i)

    for i in range(n):
        dfs(i, money, 0, set())
    return max_value


print(solution_fail(10, [[1, 1], [3, 5], [3, 5], [4, 9]]))
