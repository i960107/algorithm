from typing import List, Dict, Set
from collections import defaultdict


def solution(n: int, friends: Dict[int, Set[int]], priority: List[int]) -> int:
    seats = [[0] * (n + 1) for _ in range(n + 1)]

    for student in priority:
        r, c = choose_seat(n, friends[student], seats)
        seats[r][c] = student

    return sum([sum(row) for row in get_satisfaction_scores(n, friends, seats)])


def get_satisfaction_scores(n: int, friends: Dict[int, Set[int]], seats: List[List[int]]) -> List[List[int]]:
    satisfaction = [[0] * (n + 1) for _ in range(n + 1)]

    for r in range(1, n + 1):
        for c in range(1, n + 1):
            satisfaction[r][c] = get_satisfaction_score(n, r, c, friends[seats[r][c]], seats)

    return satisfaction


def get_satisfaction_score(n: int, r: int, c: int, friends: Set[int], seats: List[List[int]]) -> int:
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    adj_friends = 0
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        if not (1 <= nr <= n and 1 <= nc <= n):
            continue
        if not seats[nr][nc] in friends:
            continue
        adj_friends += 1

    return 10 ** (adj_friends - 1) if adj_friends > 0 else 0


def choose_seat(n: int, friends: Set[int], seats: List[List[int]]) -> List[int]:
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    # 인접하는 좋아하는 학생이 가장 많은 칸 확인
    # 그 학생을 좋아하는 학생을 알아야 함?
    # 누적된 점수를 알아야 함
    # scores = [[0] * (n + 1) for _ in range(n + 1)]
    #
    # for r in range(1, n + 1):
    #     for c in range(1, n + 1):
    #         if not seats[r][c] or seats[r][c] not in friends:
    #             continue
    #         for k in range(4):
    #             ar, ac = r + dr[k], c + dc[k]
    #
    #             if 1 <= ar <= n and 1 <= ac <= n:
    #                 scores[ar][ac] += 1

    # 인접하는 좋아하는 학생이 가장 많은 칸 확인
    candidates = []
    max_adj_friends = 0
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if seats[r][c]:
                continue
            adj_friends = 0
            for k in range(4):
                ar, ac = r + dr[k], c + dc[k]
                if not (0 <= ar < n and 0 <= ac < n):
                    continue
                if not seats[ar][ac] or seats[ar][ac] not in friends:
                    continue
                adj_friends += 1
            if adj_friends > max_adj_friends:
                candidates = [(r, c)]
                max_adj_friends = adj_friends
            elif adj_friends == max_adj_friends:
                candidates.append((r, c))

    chosen_r, chosen_c = -1, -1
    max_empty_seats = -1
    for r, c in candidates:
        empty_seats = 0
        for k in range(4):
            ar, ac = r + dr[k], c + dc[k]
            if not (0 <= ar < n and 0 <= ac < n):
                continue
            if not seats[ar][ac]:
                empty_seats += 1
        if empty_seats > max_empty_seats:
            chosen_r, chosen_c = r, c

    return [chosen_r, chosen_c]


# 각 학생의 자리를 정할때 선택할 수 있는 자리가 두군데 이상이 되는 경우가 있는가? 없음.
n = int(input())
priority = []
friends = defaultdict(set)
for student in range(1, n + 1):
    friends[student] = set(map(int, input().split()))
    priority.append(student)

print(solution(n, friends, priority))
