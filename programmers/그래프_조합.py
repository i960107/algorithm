import itertools
from typing import List


def solution_mine(n: int, k: int) -> List[List[int]]:
    # 책에서 예시 output 출력 순서가 왜 저렇게 되지?
    result = []
    path = []
    # list 만들어 둘 필요 없음
    numbers = [i + 1 for i in range(n)]

    def dfs(index: int):
        if len(path) == k:
            result.append(path[:])

        for i in range(index, len(numbers)):
            path.append(numbers[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return result


def solution(n: int, k: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            return
        # 자기 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results


print(solution_mine(4, 2))
print(solution(4, 2))
