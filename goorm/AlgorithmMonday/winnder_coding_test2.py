from typing import List
import heapq


def solution(n: int, students: List[int], points: List[int]) -> int:
    # upper = []
    # # 점수 작고, 번호 큰 순으로 pop
    # # 점수, 번호
    # # 점수를 어떻게 update하지?
    #
    # for i in range(1, n // 2 + 1):
    #     heapq.heappush(upper, (10, -i))
    # lower = []
    # # 점수 크고, 번호 작은 순으로 pop
    # for i in range(n // 2 + 1, n + 1):
    #     heapq.heappush(lower, (10, i))
    #
    # for i in range(len(students)):
    #     heapq.heapreplace()
    # 힙정렬
    # 번호 : 점수
    d = {i: 0 for i in range(1, n + 1)}
    l = [(-point, student) for student, point in d.items()]
    upper_count = n // 2
    upper = set(s for p, s in l[:upper_count])

    relocation = 0
    for student, point in zip(students, points):
        d[student] += point
        l = [(-point, student) for student, point in d.items()]
        heapq.heapify(l)
        new_upper = set(s for p,s in heapq.nsmallest(upper_count, l))
        if len(new_upper & upper) != upper_count:
            relocation += 1
        upper = new_upper

    return relocation


print(solution(6, [6, 1, 4, 2, 5, 1, 3, 3, 1, 6, 5], [3, 2, 5, 3, 4, 2, 4, 2, 3, 2, 2]))
print(solution(10, [3, 2, 10, 2, 8, 3, 9, 6, 1, 2], [3, 2, 2, 5, 4, 1, 2, 1, 3, 3]))
