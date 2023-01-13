import collections
from collections import deque
from typing import List
import heapq


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    results = []
    window = deque()
    current_max = float("-inf")

    for index, value in enumerate(nums):
        window.append(value)
        if index < k - 1:
            continue

        if current_max == float("-inf"):
            current_max = max(window)

        elif current_max < value:
            current_max = value

        results.append(current_max)

        if current_max == window.popleft():
            current_max = float("-inf")

    return results


def max_sliding_window_fail(nums: List[int], k: int) -> List[int]:
    # 최악,,,,
    max_of_window = []
    d = dict()

    for index, value in enumerate(nums):

        if index >= k - 1:
            max_num = 0
            if max_of_window and max_of_window[-1] <= value:
                max_num = value

            elif max_of_window and max_of_window[-1] >= index - k + 1:
                max_num = max_of_window[-1]
            else:
                max_num = max_in_range(nums, index - k + 1, index)
            max_of_window.append(max_num)

        d[value] = index

    return max_of_window


def max_in_range(nums: List[int], start: int, end: int) -> int:
    max_num = 0
    for index in range(start, end + 1):
        max_num = max(max_num, nums[index])
    return max_num


print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(max_sliding_window_fail([1, 3, -1, -3, 5, 3, 6, 7], 3))
# arr = [1, 3, -1, -3, 5, 3, 6, 7]
# heapq.heapify(arr)
# print(arr)
# print(heapq.heappop(arr))
#
# arr2 = [-x for x in arr]
# heapq.heapify(arr2)
# print(arr2)
# print(heapq.heappop(arr2))
