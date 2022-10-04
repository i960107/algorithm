from collections import deque, defaultdict
from typing import List, Tuple


def solution(N, M, friends: List[Tuple[int, int]]) -> int:
    '''인접 리스트 사용'''
    d_friends = defaultdict(list)
    for f1, f2 in friends:
        d_friends[f1].append(f2)
        d_friends[f2].append(f1)

    kevin_bacon = [[0] * N for _ in range(N)]

    for i in range(1, N + 1):
        q = deque((friend, 1) for friend in d_friends[i])
        while q:
            f, dist = q.popleft()
            if i != f and kevin_bacon[i - 1][f - 1] == 0:
                kevin_bacon[i - 1][f - 1] = dist
                kevin_bacon[f - 1][i - 1] = dist
                for next_f in d_friends[f]:
                    q.append((next_f, dist + 1))
    min_person, min_kevin_bacon_num = 0, N * N
    for i in range(0, N):
        cur_kevin_bacon_num = sum(kevin_bacon[i])
        if cur_kevin_bacon_num < min_kevin_bacon_num:
            min_person, min_kevin_bacon_num = i + 1, cur_kevin_bacon_num
    return min_person


def solution_2(N, M, friends: List[Tuple[int, int]]) -> int:
    '''인접 행렬 방식'''
    gr = [[False] * N for _ in range(N)]
    for f1, f2 in friends:
        gr[f1 - 1][f2 - 1] = True
        gr[f2 - 1][f1 - 1] = True
    person = -1
    min_kevin_bacon = N * N
    dist = [[0] * N for _ in range(N)]

    def bfs(start, goal):
        chk = [False] * N
        dq = deque()
        chk[start] = True
        dq.append((start, 0))
        while dq:
            now, d = dq.popleft()
            if now == goal:
                return d
            for nxt in range(N):
                # 이게 최단 길이인지 확신할 수 없음
                # if dist[nxt][goal]:
                #     d + dist[nxt][goal]

                elif gr[now][nxt] and not chk[nxt]:
                    chk[nxt] = True
                    dq.append((nxt, d + 1))

    for i in range(N):
        cur_kevin_bacon = 0
        for j in range(N):
            if i != j:
                if dist[i][j] == 0:
                    dist[i][j] = dist[i][j] = bfs(i, j)
                cur_kevin_bacon += dist[i][j]

        if min_kevin_bacon > cur_kevin_bacon:
            person = i
            min_kevin_bacon = cur_kevin_bacon

    return person + 1


N, M = 5, 5
friends = [(1, 3), (1, 4), (4, 5), (4, 3), (3, 2)]
print(solution(N, M, friends))
