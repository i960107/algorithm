from typing import List


# 최소 길이의 윈도우부터 검사해가며 윈도우 길이를 늘려가기.
# 왜 window를 사용해야하나. 매번 sum계산하는게 아니라 앞에서 하나빼고 뒤에서 하나 더하는.
# time limit exceeded -> O(N^2)이 됨.
def solution(target: int, nums: List[int]) -> int:
    for size in range(1, len(nums) + 1):
        # left inclusive, right exclusive
        left = 0
        right = size
        sub_sum = sum(nums[i] for i in range(size))
        while sub_sum < target and right < len(nums):
            sub_sum -= nums[left]
            sub_sum += nums[right]
            left += 1
            right += 1

        if sub_sum >= target:
            return size
    return 0


# 똑같이 O(N^2)아님?
def solution2(target: int, nums: List[int]) -> int:
    total = sum(nums)
    min_window_size = 0

    for size in range(len(nums), 0, -1):
        left = 0
        right = size
        sub_sum = total - sum(nums[i] for i in range(right, len(nums)))

        while sub_sum < target and right < len(nums):
            sub_sum -= nums[left]
            sub_sum += nums[right]
            left += 1
            right += 1

        if sub_sum >= target:
            min_window_size = size
        else:
            break
    return min_window_size


# start,end 포함
def solution3(target: int, nums: List[int]) -> int:
    # start inclusive end exclusive
    start = 0
    end = 1
    sub_sum = nums[0]
    while sub_sum < target and end < len(nums):
        sub_sum += nums[end]
        end += 1

    if sub_sum < target:
        return 0

    while sub_sum - nums[start] >= target:
        sub_sum -= nums[start]
        start += 1

    # 언제까지...
    # 오른쪽 포인터가 배열의 범위를 벗어나면 어쩔건데..
    min_window_size = end - start

    while start < len(nums) - 1:
        sub_sum -= nums[start]
        start += 1

        if end < len(nums):
            sub_sum += nums[end]
            end += 1

        while sub_sum - nums[end - 1] >= target:
            end -= 1
            sub_sum -= nums[end]

        if sub_sum >= target:
            min_window_size = end - start

    return min_window_size


def solution4(target, nums):
    minlen = float('inf')
    l, sum = 0, 0
    for r in range(len(nums)):
        sum += nums[r]
        while sum >= target:
            minlen = min(minlen, r - l + 1)
            sum -= nums[l]
            l += 1
    return minlen if minlen <= len(nums) else 0


# print(solution3(7, [2, 3, 1, 2, 4, 3]))
# print(solution3(2, [3]))
# # 전체를 더해야한다
# print(solution3(15, [1, 2, 3, 4, 5]))
# print(solution3(4, [1, 4, 4]))
# print(solution3(3, [1, 1]))
# print(solution3(11, [1, 2, 3, 4, 5]))
print(solution4(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
