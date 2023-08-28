from typing import List


# constant extra space ?
def solution(numbers: List[int], target: int) -> List[int]:
    def binary_search(left, right, goal: int):
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == goal:
                return mid
            elif numbers[mid] > goal:
                right = mid - 1
            else:
                left = mid + 1
        return - 1

    visited = set()
    for index, n in enumerate(numbers):
        if n in visited:
            continue

        visited.add(n)

        goal = target - n
        result = binary_search(index + 1, len(numbers) - 1, goal)
        if result != -1:
            return [index + 1, result + 1]


# dictionary 활용 -> 중복된 원소
def solution2(numbers: List[int], target: int) -> List[int]:
    d = [(n, i) for i, n in enumerate(numbers)]

    for i, n in enumerate(numbers):
        if n > target - n:
            break
        if (target - n) in d:
            return [i + 1, d[target - n]]


# 투포인터 사용
def solution3(numbers: List[int], target: int) -> List[int]:
    start = 0
    end = len(numbers) - 1
    while start < end and numbers[start] + numbers[end] != target:
        if numbers[start] + numbers[end] > target:
            end -= 1
        else:
            start += 1
    return [start + 1, end + 1]


# print(solution([2, 7, 11, 15], 9))
# print(solution([-1, 0], -1))
# print(solution([5, 25, 75], 100))
# print(solution([-1, -1, 1, 1, 1, 1, 1, 1], -2))
# print(solution([-1, 0, 1, 1, 1, 1, 1, 1], -1))
print(solution(
    [12, 13, 23, 28, 43, 44, 59, 60, 61, 68, 70, 86, 88, 92, 124, 125, 136, 168, 173, 173, 180, 199, 212, 221, 227, 230,
     277, 282, 306, 314, 316, 321, 325, 328, 336, 337, 363, 365, 368, 370, 370, 371, 375, 384, 387, 394, 400, 404, 414,
     422, 422, 427, 430, 435, 457, 493, 506, 527, 531, 538, 541, 546, 568, 583, 585, 587, 650, 652, 677, 691, 730, 737,
     740, 751, 755, 764, 778, 783, 785, 789, 794, 803, 809, 815, 847, 858, 863, 863, 874, 887, 896, 916, 920, 926, 927,
     930, 933, 957, 981, 997], 542))
