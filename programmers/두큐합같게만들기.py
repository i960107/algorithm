from typing import List
from collections import deque


def solution(queue1: List[int], queue2: List[int]) -> int:
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)

    n = len(queue1)
    m = len(queue2)

    if (sum_queue1 + sum_queue2) % 2:
        return -1

    count = 0

    # 오류나는 이유?
    # while count <= n:
    # 2 ^ n 경우의 수가 있지 않나?
    while count <= 2 * n + m:
        if sum_queue1 == sum_queue2:
            return count

        elif sum_queue1 < sum_queue2:
            popped = queue2.popleft()
            sum_queue2 -= popped
            queue1.append(popped)
            sum_queue1 += popped

        elif sum_queue1 > sum_queue2:
            popped = queue1.popleft()
            sum_queue1 -= popped
            queue2.append(popped)
            sum_queue2 += popped

        count += 1

    return -1


# 보완 필요!!
def solution_two_pointer(queue1: List[int], queue2: List[int]) -> int:
    total = sum(queue1) + sum(queue2)
    if total % 2 == 1:
        return - 1

    queue = deque(queue1)
    queue.extend(queue2)

    left, right = 0, len(queue) - 1

    sum_in_range = sum(queue)
    target = sum_in_range // 2

    count = 0
    while left < right:
        if sum_in_range == target:
            return count
        if sum_in_range < target:
            right += 1
        elif sum_in_range > target:
            left += 1
        count += 1
    return -1
