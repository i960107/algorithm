from typing import List
from collections import defaultdict, deque


def solution(begin: str, target: str, words: List[str]) -> int:
    adj = defaultdict(list)

    for word in words:
        if sum(1 for x, y in zip(begin, word) if x != y) == 1:
            adj[begin].append(word)
            adj[word].append(begin)

    for i in range(len(words)):
        a = words[i]
        for j in range(i + 1, len(words)):
            b = words[j]
            if sum(1 for x, y in zip(a, b) if x != y) == 1:
                adj[a].append(b)
                adj[b].append(a)

    queue = deque()
    queue.append((begin, 0))

    visited = set()
    while queue:
        curr, distance = queue.popleft()

        if curr in visited:
            continue

        if curr == target:
            return distance

        visited.add(curr)

        for next in adj[curr]:
            queue.append((next, distance + 1))

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
