from typing import List
import heapq


def solution(k: int, score: List[int]) -> List[int]:
    queue = []
    answer = []
    for now_score in score:
        if len(queue) < k:
            heapq.heappush(queue, now_score)
        else:
            heapq.heappushpop(queue, now_score)
        answer.append(queue[0])
    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
