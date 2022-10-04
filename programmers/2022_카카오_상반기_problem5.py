from typing import List, Deque
from collections import deque


def solution(rc: List[List[int]], operations: List[str]) -> List[List[int]]:
    row, column = len(rc), len(rc[0])
    queue = deque(rc)

    # 로테이트시 대상이 되는 원소들의 개수 가장 외각의 원소의 개숫
    rotate_element_count = row * 2 + (column - 2) * 2

    def shift_row():
        queue.insert(0, queue.pop())

    def rotate():
        i, j = 0, 1
        prev = queue[0][0]

        count = rotate_element_count
        while count > 0:
            temp = queue[i][j]
            queue[i][j] = prev
            prev = temp
            if i == 0 and j < column - 1:
                j += 1
            elif j == column - 1 and i < row - 1:
                i += 1
            elif i == row - 1 and j > 0:
                j -= 1
            else:
                i -= 1
            count -=1

    for op in operations:
        if op == "Rotate":
            rotate()
        elif op == "ShiftRow":
            shift_row()

    return list(queue)


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
