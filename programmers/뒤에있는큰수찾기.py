from typing import List


# brute - force는 O(N^2)
def solution(numbers: List[int]) -> List[int]:
    n = len(numbers)
    answer = [-1] * len(numbers)
    stack = []
    for index, number in enumerate(numbers):
        if not stack or numbers[stack[-1]] >= number:
            stack.append(index)
            continue
        while stack and numbers[stack[-1]] < number:
            popped_index = stack.pop()
            answer[popped_index] = number
        stack.append(index)
    return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
