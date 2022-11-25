from typing import List


def solution(histogram: List[int]) -> int:
    stack = []
    answer = [0] * len(histogram)
    # 내림차순 정렬해 보자
    for index, height in enumerate(histogram):
        while stack and histogram[stack[-1]] < height:
            max_index = stack.pop()
            max_height = histogram[max_index]
        answer[index] = max(answer[index], height, stack[-1])


    return 0


print(solution([2, 1, 3, 4, 1]))
print(solution([6, 3, 1, 4, 12, 4]))
print(solution([5, 6, 7, 4, 1]))
