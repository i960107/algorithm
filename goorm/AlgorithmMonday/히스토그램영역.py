from typing import List


def solution(histogram: List[int]) -> int:
    stack = []
    answer = [0] * len(histogram)

    # 내림차순 정렬해 보자
    def _solution(index: int, height: int) -> int:
        # 스택 원소들과 비교해서 현재
        if len(stack) == 1:
            return height * (index + 1)
        max_area = 0
        for prev_index in stack:
            prev_height = histogram[prev_index]
            max_area = max(max_area, (index - prev_index + 1) * prev_height)
        return max_area

    for index, height in enumerate(histogram):
        while stack and histogram[stack[-1]] >= height:
            max_index = stack.pop()
            max_height = histogram[max_index]
        stack.append(index)
        answer[index] = _solution(index, height)

    print(answer)
    return max(answer)


print(solution([2, 1, 3, 4, 1]))
print(solution([6, 3, 1, 4, 12, 4]))
print(solution([5, 6, 7, 4, 1]))
