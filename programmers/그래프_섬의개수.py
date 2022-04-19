from typing import List


def get_number_of_island(grid: List[List[str]]) -> int:
    # 입력값이 정확히 인접행렬로 표현된 그래프는 아니지만
    # 사실상 동서남북이 모두 연결된 그래프로 가정하고 동일한 형태로 처리할 수 있음
    # 네 방향 각각 DFS 재귀를 이용해 탐색을 끝마치면 1이 증가하는 형태로 육지의 개수를 파악
    def dfs(i: int, j: int):
        # 더이상 땅이 아닌 경우 종료
        # 매 4경우마다 체크해야하는 것 아닌가?
        # 매 4경우 재귀 호출 전 체크 혹은 재귀 호출후 예외처리 해주면 됨!
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
            return
        # 이미 탐색한 곳 0으로 변경!
        grid[i][j] = 0
        # 동서남북 탐색
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    if not grid:
        return count
    # None type has no len() 예외처리 필요
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                # 모든 육지 탐색 후 카운트 1 증가!
                dfs(i, j)
                count += 1
    return count


def solution_test(grid: List[List[str]]) -> int:
    answer = 0

    # 언제 count 증가시킬지가 문제군!
    def dfs(r: int, c: int):
        if grid[r][c] == "0":
            return
        grid[r][c] = "0"
        if r - 1 >= 0:
            dfs(r - 1, c)
        if r + 1 < len(grid):
            dfs(r + 1, c)
        if c - 1 >= 0:
            dfs(r, c - 1)
        if c + 1 < len(grid[r]):
            dfs(r, c + 1)

    if not grid:
        return answer
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # 이미 탐색한 곳이면 값이 0
            if grid[i][j] == "1":
                dfs(i, j)
                answer += 1
    return answer


print(get_number_of_island(None))
print(get_number_of_island(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))  # 1
print(get_number_of_island(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))  # 3

print(solution_test(None))
print(solution_test(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))  # 1
print(solution_test(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))  # 3
