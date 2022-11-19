from typing import List
from sys import stdin


def solution(n, k, words: List[str]):
    return sorted(words, key=lambda x: (len(x), x))[k - 1]


read = stdin.readline

n, k = map(int, input().split())
words = []
for _ in range(n):
    words.append(read())
print(solution(n, k, words))
