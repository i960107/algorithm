from itertools import permutations
from typing import List


def solution(nums: List[int], operation_count: List[int]) -> List[int]:
    '''brute force'''
    min_result = 1000000001
    max_result = -1000000001

    print(permutations([]))

    return [min_result, max_result]


def solution_dfs(nums: List[int], operation_count: List[int]) -> List[int]:
    '''dfs'''
    min_result = 1000000001
    max_result = -1000000001

    def evaluate(num1: int, num2: int, operator: int) -> int:
        if operator == 0:
            return num1 + num2
        elif operator == 1:
            return num1 - num2
        if operator == 2:
            return num1 * num2
        if operator == 3:
            if num1 < 0 and num2 > 0:
                return -num1 // num2
            else:
                return num1 // num2

    def dfs(res: int, nums_left: List[int], operations_left: List[int]) -> int:
        nonlocal min_result, max_result
        if not nums_left:
            min_result = min(min_result, res)
            max_result = max(max_result, res)

        for i, cnt in enumerate(operations_left):
            if cnt > 0:
                op_left = operations_left[:]
                op_left[i] -= 1
                dfs(evaluate(res, nums_left[0], i),
                    nums_left[1:],
                    op_left)

    dfs(nums[0], nums[1:], operation_count)

    return [min_result, max_result]


def solution_bfs(nums: List[int], operation_count: List[int]) -> List[int]:
    pass

print(solution_dfs([5, 6], [0, 0, 1, 0]))
print(solution_dfs([3, 4, 5], [1, 0, 1, 0]))
print(solution_dfs([1, 2, 3, 4, 5, 6], [2, 1, 1, 1]))
