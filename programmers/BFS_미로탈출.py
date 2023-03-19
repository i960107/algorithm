from typing import List
import heapq


'''다익스트라풀이'''
# S -> L, L->E로 bfs두번 돌릴 수 있음. O(N)
# 다익스트라 -> O(NlogN)
def solution(maps: List[str]) -> int:
    INF = int(1e9)
    R, C = len(maps), len(maps[0])

    queue = []
    # 레버를 밟지 않고, 밟고
    distances = [[[INF, INF] for _ in range(C)] for _ in range(R)]

    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    E = None
    for r in range(R):
        for c in range(C):
            if maps[r][c] == "S":
                queue.append((0, r, c, False))
                distances[r][c][False] = 0
            elif maps[r][c] == "E":
                E = [r, c]

    # 여러번 지나갈 수 있음...?
    # 레버를 밟고 지나가니 밟지 않고 지나가기 둘다 세어줘야함.
    while queue:
        dist, r, c, lever = heapq.heappop(queue)

        if distances[r][c][lever] < dist:
            continue

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            nxt_dist = dist + 1

            if not (0 <= nr < R and 0 <= nc < C):
                continue

            nxt_lever = (lever or maps[nr][nc] == "L")

            if maps[nr][nc] == "X":
                continue

            if distances[nr][nc][nxt_lever] <= nxt_dist:
                continue

            heapq.heappush(queue, (nxt_dist, nr, nc, nxt_lever))
            distances[nr][nc][nxt_lever] = nxt_dist

    distance = distances[E[0]][E[1]][True]
    return distance if distance != INF else -1


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))
