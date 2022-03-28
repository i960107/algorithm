from typing import List


def solution(arr1: List[List], arr2: List[List]) -> List[List]:
    answer = [[None] * len(arr2[0]) for _ in range(len(arr1))]

    for row in range(len(answer)):
        for column in range(len(answer[row])):
            multiplied = 0
            # zip보다 3중 for문이 더 빠름 왜?
            for k in range(len(arr2)):
                multiplied += arr1[row][k] * arr2[k][column]
            answer[row][column] = multiplied
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
