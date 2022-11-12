from typing import List


def get_successful_candidates_number(n: int, scores: List[int]) -> int:
    avg_score = sum(scores) / n
    return sum([1 for s in scores if s >= avg_score])


t = int(input())

for _ in range(t):
    n = int(input())
    scores = list(map(int, input().split()))
    print("%d/%d" % (get_successful_candidates_number(n, scores), n))
