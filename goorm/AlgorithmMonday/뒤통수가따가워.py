from typing import List


def solution(n: int, summits: List[int]) -> List[int]:
    stack = []
    answer = []

    def pop_until_larger_element(value: int) -> int:
        popped = 0
        while stack and stack[-1] <= value:
            stack.pop()
            popped += 1
        return popped

    for s in summits:
        answer.append(len(stack))
        pop_until_larger_element(s)
        stack.append(s)
    return answer


def solution2(n: int, summits: List[int]) -> List[int]:
    answer = []
    max_heights = []
    answer.append(0)
    max_heights.append((0, summits[0]))

    for curr_index in range(1, len(summits)):
        curr_height, (max_index, max_height) = summits[curr_index], max_heights[curr_index - 1]
        if max_height >= curr_height:
            curr = (max_index, max_height)
        else:
            curr = (curr_index, curr_height)
        answer.append(curr_index - max_index)
        max_heights.append(curr)
    print(answer)
    print(max_heights)
    return answer


# n = int(input())
# summits = list(map(int, input().split()))
summits = [4, 4, 3, 2, 4]
print(*solution(5, summits))
print(*solution2(5, summits))
