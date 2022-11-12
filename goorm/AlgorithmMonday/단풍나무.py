from typing import List, Final
from collections import deque


# def get_day_required_to_all_maples_be_tinged(N: int, grid: List[List[int]]) -> int:
#     dj = (0, 0, -1, 1)
#     di = (1, -1, 0, 0)
#
#     # 좌표 i,j, 체크된 가장 최근 날짜
#     tinged_area = deque()
#     untinged_maples = 0
#     for i in range(N):
#         for j in range(N):
#             if grid[i][j] == 0:
#                 tinged_area.append((i, j, 0))
#             if grid[i][j]:
#                 untinged_maples += grid[i][j]
#
#     while tinged_area:
#
#         i, j, day = tinged_area.popleft()
#         nd = day + 1
#
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#
#             if 0 <= ni < N and 0 <= nj < N and grid[ni][nj]:
#                 grid[ni][nj] -= 1
#                 untinged_maples -= 1
#
#                 if grid[ni][nj] == 0:
#                     tinged_area.append((ni, nj, nd))
#
#             tinged_area.append((i, j, nd))
#
#         if untinged_maples == 0:
#             return nd
#
#     return total_day


class MaplePark:
    DY: Final = (0, 0, -1, 1)
    DX: Final = (1, -1, 0, 0)

    def __init__(self, N: int, park: List[List[int]]):
        self.N = N
        self.park = park

    def is_all_colored(self) -> bool:
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                if self.park[i][j]:
                    return False
        return True

    def get_days_for_all_maples_to_tinged(self) -> int:
        if self.is_all_colored():
            return 0
        # 그날 밤에 각 구역에서 물들게 될 단풍나무 수
        update = [[0] * (1 + self.N) for _ in range(self.N + 1)]
        day = 1

        # 나무가 모두 물들때까지 시뮬레이션
        while True:
            for i in range(1, self.N + 1):
                for j in range(1, self.N + 1):
                    for k in range(4):
                        nj, ni = j + self.DX[k], i + self.DY[k]
                        if 1 <= nj <= self.N and 1 <= ni <= self.N and self.park[ni][nj] == 0:
                            update[i][j] += 1

            self.update_colored_maples_at_the_day(update)

            if self.is_all_colored():
                break

            day += 1
        return day

    def update_colored_maples_at_the_day(self, update: List[List[int]]):
        '''그날 물든 단풍나무 수를 반영하고 update값 초기화'''
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                self.park[i][j] = max(0, self.park[i][j] - update[i][j])
                update[i][j] = 0


N = int(input())
grid = []
parks = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    grid.append(line)
    for j in range(1, N + 1):
        parks[i][j] = line[j - 1]

mp = MaplePark(N, parks)
print(mp.get_days_for_all_maples_to_tinged())
print(get_day_required_to_all_maples_be_tinged(N, grid))
