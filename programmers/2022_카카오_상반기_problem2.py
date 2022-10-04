from typing import List
from itertools import combinations
from collections import deque


def solution(queue1: List[int], queue2: List[int]) -> int:
    q1 = deque(queue1)
    sum1 = sum(queue1)
    q2 = deque(queue2)
    sum2 = sum(queue2)

    target = (sum1 + sum2) / 2

    if target != int(target):
        return -1
    else:
        target = int(target)

    if sum1 == target:
        return 0

    # 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우
    # 트리로 조합해서 target을 만들 수 있는지 검사하기?

    count = 0

    def can_make_target(csum: int, index: int, path: List[int]):
        if csum > target:
            return False

        if csum == target:
            return True

        for i in range(index, len(candidates)):
            if can_make_target(csum + candidates[i], i + 1, path + [candidates[i]]):
                return True

        return False

    candidates = queue1 + queue2

    if not can_make_target(0, 0, []):
        return -1

    #queue1 < target이라고 q1에서 원소를 꺼내는게 전체 결과를 최소로 만드는 것 아님.
    while True:

        # sorted_q1 = "".join(map(str, sorted(q1)))

        # 그냥 합을 history에 넣으면 안됨!
        # list not hashanble
        # 시간 초과남
        # if sorted_q1 in history:
        #     break
        # else:
        #     history.add(sorted_q1)

        if sum1 == target:
            return count

        elif sum1 < target:
            element = q2.popleft()
            sum2 -= element
            q1.append(element)
            sum1 += element

        else:
            element = q1.popleft()
            sum1 -= element
            q2.append(element)
            sum2 += element

        count += 1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
