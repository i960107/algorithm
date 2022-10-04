from typing import List


def solution(nums: List[int]) -> List[int]:
    answer = [-1] * len(nums)
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)
    return answer


print(solution([3, 5, 2, 7]))
print(solution([9, 5, 4, 8]))
