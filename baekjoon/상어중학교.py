from typing import List, Dict
from collections import defaultdict


def solution(n: int, friends: Dict[List[int]]) -> int:
    seats = [[0] * (n + 1) for _ in range(n + 1)]
    pass


n = int(input())
friends = defaultdict(list)
for student in range(1, n + 1):
    friends[student] = list(map(int, input().split()))

print(solution(n, friends))
