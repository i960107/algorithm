from collections import deque

'''바이러스'''


class State:
    def __init__(self, population: int, time_spent: int):
        self.population = population
        self.time_spent = time_spent


# 개체수가 정확히 goal마리가 되기 위해 필요한 최소 시간
def get_minimum_time_required(target_number: int) -> int:
    MAXIMUM_VIRUS = 100000

    bfs_queue = deque()
    bfs_queue.append(State(1, 0))

    min_time_required = [0] * (MAXIMUM_VIRUS + 1)
    visited = [False] * (MAXIMUM_VIRUS + 1)

    while bfs_queue:
        # visited를 관리할 필요가 있을까, 배열로? set으로
        current = bfs_queue.popleft()

        if current.population > MAXIMUM_VIRUS:
            continue

        if visited[current.population]:
            continue

        visited[current.population] = True
        min_time_required[current.population] = current.time_spent

        next_increase = current.population * 2
        next_decrease = current.population // 3

        bfs_queue.append(State(next_increase, current.time_spent + 1))
        bfs_queue.append(State(next_decrease, current.time_spent + 1))

    return bfs_queue[target_number]


t = int(input())
for _ in range(t):
    goal = int(input())
    print(get_minimum_time_required(goal))
