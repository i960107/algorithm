from typing import List
from itertools import combinations
from collections import Counter


# def solution_1(grid: List[str]) -> int:
#     answer = 0
#     grid = [list(x) for x in grid]
#     # i는 행 j는 열을 나타냄
#     for i in range(len(grid)):
#         # 행의 수 == 열의 수 같음
#         for j in range(len(grid[i])):
#             # 값을 가지고 있다면
#             if grid[i][j] != '?':
#                 continue
#             # 값이 ? 일때
#             else:
#                 up = grid[i - 1][j] if i - 1 >= 0 else None
#                 down = grid[i + 1][j] if i + 1 < len(grid) else None
#                 left = grid[i][j - 1] if j - 1 >= 0 else None
#                 right = grid[i][j + 1] if j + 1 < len(grid) else None
#                 counter = Counter(element for element in [up, down, left, right] if element)
#                 # 2개 이상 같다면 무조건 그 원소 될 수 있음
#                 # 다 다르다면 원소의 개수만큼 가능
#                 # 2개 이상의 인접한 유효한 값을 가지고 그 값들 중 중복값이 있을때
#                 # 인접한 값이 하나라면
#                 if len(counter) == 0:
#                     list(counter.keys())[0] != "?":
#                     grid[i][j] = list(counter.keys())[0]
#                 # 인접한 값이 두개라면
#                 if len(counter) == 2:
#                 # 인거
#                 for element, cnt in counter.items():
#                     if element == "?":
#                         continue
#                     if cnt >= 2:
#                         grid[i][j] = element
#                         break
#
#     print(grid)
#     return answer


def solution(grid: List[str]) -> int:
    answer = 0
    l_grid = []
    unknown = []
    for i in range(len(grid)):
        curr = []
        for j, y in enumerate(grid[i]):
            curr.append(y)
            if y == "?":
                unknown.append((i, j))
        l_grid.append(curr)
    print(unknown)

    i_unknown = 0
    while len(unknown) > 0:
        i, j = unknown[i_unknown]
        up = grid[i - 1][j] if i - 1 >= 0 else None
        down = grid[i + 1][j] if i + 1 < len(grid) else None
        left = grid[i][j - 1] if j - 1 >= 0 else None
        right = grid[i][j + 1] if j + 1 < len(grid) else None
        counter = Counter(element for element in [up, down, left, right] if element)
        if len(counter) == 1:
            
        elif len(counter) == 2:
            pass
        else:
            pass

        i_unknown = (i_unknown + 1) % i_unknown


return answer

print(solution(["aa?"]))  # 3

print(solution(["??b", "abc", "cc?"]))  # 2
print(solution(["abcabcab", "????????"]))  # 0
print(solution(["?"]))  # 0
