from typing import List


def solution(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


print(solution([2, 2, 1]))
print(solution([4, 1, 2, 1, 2]))
