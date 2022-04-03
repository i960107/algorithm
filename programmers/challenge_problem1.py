from typing import List


def solution(dist: List[List[int]]) -> List[List[int]]:
    max_distance = 0
    # i < j
    max_distance_elements = (0, 0)
    for i in range(len(dist)):
        for j in range(i + 1, len(dist)):
            if dist[i][j] > max_distance:
                max_distance = dist[i][j]
                max_distance_elements = (i, j)

    dots = list(range(len(dist)))
    result = [dot for _, dot in sorted(zip(dist[max_distance_elements[1]], dots), reverse=True)]

    return [result, result[::-1]]


print(solution(
    [[0, 5, 2, 4, 1],
     [5, 0, 3, 9, 6],
     [2, 3, 0, 6, 3],
     [4, 9, 6, 0, 3],
     [1, 6, 3, 3, 0]]))  # [[1,2,0,4,3],[3,4,0,2,1]]
print(solution(
    [[0, 2, 3, 1],
     [2, 0, 1, 1],
     [3, 1, 0, 2],
     [1, 1, 2, 0]]))  # [[0,3,1,2],[2,1,3,0]]

# 테스트용
print(solution([[0, 4], [4, 0]]))
