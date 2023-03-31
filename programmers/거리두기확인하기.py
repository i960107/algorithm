from typing import List
from collections import deque


def solution(places: List[List[str]]) -> List[int]:
    PERSON = "P"
    EMPTY = "O"
    PARTITION = "X"

    n = 5
    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)

    def bfs(place: List[str], r, c, visited: List[List[bool]]) -> bool:
        queue = deque()
        queue.append((r, c, 0))

        while queue:
            cr, cc, depth = queue.popleft()

            for k in range(4):
                nr, nc, ndepth = cr + dr[k], cc + dc[k], depth + 1
                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                if visited[nr][nc] or ndepth > 2 or place[nr][nc] == PARTITION:
                    continue
                if place[nr][nc] == PERSON:
                    return False
                queue.append((nr, nc, ndepth))
                visited[nr][nc] = True

        return True

    answer = []
    for place in places:
        found_illegal = False
        visited = [[False] * n for _ in range(n)]
        for r in range(n):
            if found_illegal:
                break
            for c in range(n):
                if place[r][c] != PERSON or visited[r][c]:
                    continue
                visited[r][c] = True
                result = bfs(place, r, c, visited)
                if not result:
                    found_illegal = True
                    break
        answer.append(int(not found_illegal))
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
