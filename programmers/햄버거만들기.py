from typing import List


def solution(ingredient: List[int]) -> int:
    # 1,2,3,1일때 pop
    stack = []
    # 순서도 중요! counter만으로는 의미없음!
    # included = dict()

    hamburgers = 0
    for i in range(len(ingredient)):
        now = ingredient[i]
        stack.append(now)
        if len(stack) < 4:
            continue
        if stack[-4:] != [1,2,3,1]:
            continue
        hamburgers += 1
        for _ in range(4):
            stack.pop()

    return hamburgers


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
