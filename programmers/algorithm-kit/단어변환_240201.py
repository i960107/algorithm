from typing import List
from collections import deque


def solution(begin: str, target: str, words: List[str]) -> int:
    n = len(begin)
    queue = deque()
    queue.append((begin, 0))
    visited = set()
    while queue:
        now, dist = queue.popleft()

        if now in visited:
            continue

        if now == target:
            return dist

        visited.add(now)

        for nxt in words:
            diff = 0
            for i in range(n):
                if nxt[i] != now[i]:
                    diff += 1
                if diff == 2:
                    break
            if diff == 2:
                continue

            queue.append((nxt, dist + 1))
    return 0


# 단어변환, leetcode edit distance
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
