from typing import List


def solution(nums: List[int], M: int, K: int) -> int:
    nums.sort(reverse=True)
    return nums[0] * M // (K + 1) * K + nums[1] * M // (K + 1)


def solution2(nums: List[int], M: int, K: int) -> int:
    nums.sort(reverse=True)
    s = [nums[0]] * K + [nums[1]]
    count = M // (K + 1)
    print(s, count, M - (K + 1) * count)

    return sum(s) * count + sum(s[:M - (K + 1) * count])


res = solution([2, 4, 5, 4, 6], 8, 3)
res2 = solution2([2, 4, 5, 4, 6], 8, 3)
print(res2)
print(res == res2)
