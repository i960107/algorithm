from collections import defaultdict
from typing import List


def solution(servers: int, sticky: bool, request: List[int]) -> List[List[int]]:
    answer = [[] for _ in range(servers)]
    sticked = dict()
    curr = 0
    for i in range(len(request)):
        if sticky and request[i] in sticked:
            answer[sticked[request[i]]].append(request[i])

        else:
            answer[curr].append(request[i])
            sticked[request[i]] = curr
            curr = (curr + 1) % servers
    return answer


print(solution(2, False, [1, 2, 3, 4]))
print(solution(2, True, [1, 1, 2, 2]))
print(solution(2, True, [1, 2, 2, 3, 4, 1]))
