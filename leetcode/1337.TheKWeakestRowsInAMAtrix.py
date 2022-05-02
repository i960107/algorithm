import bisect
from typing import List


def KWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    # 정렬되지 않았기 때문에 어려움..
    # 내림차순 정렬된 배열에서 이진검색?
    # 선형 검색 이 나을 수도 100개 row
    soldiers = [(len(mat[row]) - bisect.bisect_left(sorted(mat[row]), 1), row) for row in range(len(mat))]
    soldiers.sort()
    return [row for _, row in soldiers[:k]]


print(KWeakestRows(mat=
                   [[1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1]],
                   k=3))
