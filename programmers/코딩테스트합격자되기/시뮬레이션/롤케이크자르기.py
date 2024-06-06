from typing import List
from collections import Counter, defaultdict


def solution(topping: List[int]) -> int:
    right = Counter(topping)

    # 전체가 같은 종류일때도 있음 주의!
    # if (len(right) % 2 != 0):
    #     return 0

    answer = 0
    left = defaultdict(int)
    for i in range(len(topping)):
        curr = topping[i]
        left[curr] += 1
        right[curr] -= 1
        if right[curr] == 0:
            right.pop(curr)
        if len(left) == len(right):
            answer += 1
        # 더 나아가면 right는 줄어들 수 밖에 없으므로 한번 추월하면 더 이상 같은 종류 가질 수 없게 됨.
        if len(left) > len(right):
            break
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))
print(solution([1, 2, 3, 1, 2]))
print(solution([1, 2, 1, 3, 1, 1, 1, 4, 1, 2]))
print(solution([1, 1]))
