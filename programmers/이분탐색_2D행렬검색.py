from typing import List


def search_2d_matrix(matrix: List[list], target: int) -> bool:
    '''m*n 행렬에서 값을 찾아내는 호율적인 알고리즘.행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순 정렬되어있다.'''
    # 에외처리
    if not matrix:
        return False
    row = 0
    # 각 행에 대해서 이진검색하는 것 O(NlogN)
    # 첫 행의 맨 뒤부터 탐색 시작. O(N)
    # 첫 행의 맨 처음부터 시작해도 됨? 안됨. 행렬은 왼쪽에서 오른쪽, 위에서 아래로 오름차순 정렬되어 있기 때문에
    # 왼쪽으로 이동->작아짐. 밑으로 이동하면 ->커짐
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if target == matrix[row][col]:
            return True
        elif target > matrix[row][col]:
            row += 1
        else:
            col -= 1
    return False


def search_2d_matrix_pythonic(matrix: List[list], target: int) -> bool:
    # O(N)
    return any(target in row for row in matrix)


print(search_2d_matrix([[1, 4, 7, 11, 15],
                        [2, 5, 8, 12, 19],
                        [3, 6, 9, 16, 22],
                        [10, 13, 14, 17, 24],
                        [18, 21, 23, 26, 30]],
                       5))
