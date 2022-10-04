from typing import List


def solution(nums: List[int]) -> List[int]:
    nums.sort()
    remove = sum(nums) - 100
    p1, p2 = 0, len(nums) - 1

    while nums[p1] + nums[p2] != remove:

        if nums[p1] + nums[p2] > remove:
            p2 -= 1

        elif nums[p1] + nums[p2] < remove:
            p1 += 1

    return [num for i, num in enumerate(nums) if i not in (p1, p2)]


res = solution([7, 8, 10, 13, 15, 19, 20, 23, 25])
print(res, res == [7, 8, 10, 13, 19, 20, 23])
