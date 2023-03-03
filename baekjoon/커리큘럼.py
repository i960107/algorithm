from typing import List
from collections import defaultdict, deque


def solution(N: int, lectures: List[int]) -> List[int]:
    pass


N = int(input())
d = defaultdict(list)
times = [0] * (N + 1)
indegree = [0] * (N + 1)

for i in range(1, N + 1):
    time, *priors, end = map(int, input().split())
    times[i] = time
    indegree[i] += len(priors)
    for prior in priors:
        d[prior].append(i)

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append((i, times[i]))

# 각 강의를 수강하기까지 최소시간
required = [0] * (N + 1)
while queue:
    curr, accumulated = queue.popleft()
    required[curr] = max(required[curr], accumulated)

    for next in d[curr]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append((next, accumulated + times[next]))

for i in range(1, N + 1):
    print(required[i])
