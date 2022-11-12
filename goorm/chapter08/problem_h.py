from typing import List, Final
from collections import deque

'''단지 번호 붙이기'''


# @brief (r행 c열)의 집으로부터 연결된 '아직 방문하지 않은 집'의 총 수를 계산하는 함수
# 이 과정에서 방문하는 집은 모두 visited[r][c]를 true로 갱신한다
def get_linked_houses_number(r: int, c: int, N: int, is_house: List[List[bool]], visited: List[List[int]]) -> int:
    if r < 1 or c < 1 or r > N or c > N:
        return 0

    elif not is_house[r][c] or visited[r][c]:
        return 0

    visited[r][c] = True

    count = 1
    # 상하좌우로 인접한 집으로부터 연결된 집의 수를 재귀적으로 계산하여 가산한다
    count += get_linked_houses_number(r - 1, c, N,is_house, visited)
    count += get_linked_houses_number(r + 1, c, N,is_house, visited)
    count += get_linked_houses_number(r, c - 1, N,is_house, visited)
    count += get_linked_houses_number(r, c + 1, N,is_house, visited)

    return count


# @brief 문제의 조건에 따라 지도에 존재하는 모든 단지들의 크기를 반환하는 함수
def get_all_group_sizes(is_house: List[List[bool]], N: int) -> List[int]:
    group_sizes = []
    # 집이 있어도 방문했다면 이미 탐색된 영역에 속함
    visited = [[False] * (N + 2) for _ in range(N + 2)]

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if is_house[row][col] and not visited[row][col]:
                size = get_linked_houses_number(row, col, N, is_house, visited)
                group_sizes.append(size)

    group_sizes.sort()
    return group_sizes


N = int(input())
is_house = [[False] * (N + 2) for _ in range(N + 2)]

for row in range(1, N + 1):
    line = input().split()
    for col in range(1, N + 1):
        x = line[col - 1]
        if x == "1":
            is_house[row][col] = True

group_sizes = get_all_group_sizes(is_house, N)

print(len(group_sizes))
for size in group_sizes:
    print(size)
