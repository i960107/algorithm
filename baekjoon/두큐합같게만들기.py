from typing import List
from collections import deque


def solution(queue1: List[int], queue2: List[int]) -> int:
    target = (sum(queue1) + sum(queue2)) / 2
    if target != int(target):
        return -1

    def _solution(first_queue, last_queue):
        n, m = len(first_queue), len(last_queue)

        prefix = [0] * (n + m + 1)

        for i, x in enumerate(first_queue, 1):
            prefix[i] = prefix[i - 1] + x

        for i, x in enumerate(last_queue, 1):
            prefix[n + i] = prefix[n + i - 1] + x

        minimum_job = int(1e9)
        for j, end in enumerate(prefix):
            if end < target:
                continue
            for i in range(i + 1):
                if prefix[j] - prefix[i - 1] == target:
                    job = 0
                    if minimum_job > job:
                        minimum_job = job
                    break
        return minimum_job

    return min(_solution(queue1, queue2), _solution(queue2, queue1))


# 복잡도는?
# 더 좋은 방법 없을까?
def solution2(queue1: List[int], queue2: List[int]) -> int:
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    target = (sum_queue1 + sum_queue2) // 2
    if target != int(target):
        return -1

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    job = 0
    while queue1 and queue2:
        if sum_queue1 == target:
            break

        if sum_queue1 > target:
            popped = queue1.popleft()
            sum_queue1 -= popped
            queue2.append(popped)
            sum_queue2 += popped
        else:
            popped = queue2.popleft()
            sum_queue2 -= popped
            queue1.append(popped)
            sum_queue1 += popped
        job += 1
    if sum_queue1 != target:
        return - 1
    return job


print(solution2([3, 2, 7, 2], [4, 6, 5, 1]))
