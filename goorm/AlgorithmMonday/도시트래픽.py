from typing import List, Dict, Set
from collections import defaultdict


def convert_to_adj_list(strArr: List[str]) -> Dict[int, List[int]]:
    adj = dict()
    for x in strArr:
        key, value = x.split(":")
        adj[int(key)] = list(map(int, value[1:-1].split(",")))
    return adj


def solution(strArr: List[str]) -> str:
    adj = convert_to_adj_list(strArr)
    answer = defaultdict(int)

    def _dfs(node: int, visited: Set[int]) -> int:
        if node in visited:
            return 0

        nonlocal answer
        visited.add(node)

        max_traffic = 0
        for next in adj[node]:
            max_traffic += node + _dfs(next, visited)
        answer[node] = max_traffic

        visited.remove(node)

        return max_traffic

    for city in adj:
        _dfs(city, set())

    print(answer)
    return ""


print(solution(["1:[5]", "4:[5]", "3:[5]", "5:[1,4,3,2]", "2:[5,15,7]", "7:[2,8]", "8:[7,38]", "15:[2]", "38:[8]"]))
# print(solution(["1:[5]", "2:[5]", "3:[5]", "4:[5]", "5:[1,2,3,4]"]))
# print(solution(["1:[5]", "2:[5,18]", "3:[5,12]", "4:[5]", "5:[1,2,3,4]", "18:[2]", "12:[3]"]))
