from typing import List

'''놀이 공원'''


def solution(n: int, k: int, area: List[List[int]]) -> int:
    # 투포인터 슬라이딩 윈도우?
    # 폐기물 입장에서 영향을 끼칠 수 있는 곳들 - bfs?
    answer = 0
    return answer


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    area = []
    for _ in range(n):
        area.append(list(map(int, input().split())))
    res = solution(n, k, area)
    print(res)