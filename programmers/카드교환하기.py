from typing import Dict
from collections import defaultdict
from sys import stdin


def solution(cards: Dict, relations: Dict) -> int:
    pass



n, m = map(int, input().split())
read = stdin.readline
cards = dict()
for _ in range(n):
    i, ci = map(int, read().split())
    cards[i] = ci

relations = defaultdict(list)
for _ in range(m):
    u, v = map(int, read().split())
    relations[u].append(v)
    relations[v].append(u)

solution(cards, relations)
