from typing import List


# constant extra space ?

def solution(numbers: List[int], target: int) -> List[int]:
    def binary_search(left, right, goal: int):
        while left <= right:
            mid = (left + right) // 2
            if (numbers[mid] == goal):
                return mid
            elif numbers[mid] > goal:
                right = mid - 1
            else:
                left = mid + 1
        return - 1

    for index, n in enumerate(numbers):
        goal = target - n
        result = binary_search(index + 1, len(numbers), goal)
        if result != -1:
            return [index + 1, result + 1]


print(solution([2, 7, 11, 15], 9))
