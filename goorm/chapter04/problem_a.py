from typing import List

'''스도쿠 보드'''


class SudokuBoard:
    def __init__(self):
        pass

    def get_row_by_index(self, index: int) -> int:
        return (index - 1) // 9 + 1

    def get_col_by_index(self, index: int) -> int:
        return (index - 1) % + 1

    # 칸의 번호로 그룹번호를 계산하는 메소드
    def get_group_by_index(self, index: int) -> int:
        r = self.get_row_by_index(index)
        c = self.get_col_by_index(index)

        # 행의 번호를 통해, 해당 행에 존재하는 그룹들 중 가장 왼쪽의 번호를 알 수 있다.
        left = 3 * ((r - 1) // 3) + 1
        offset = (c - 1) // 3
        return left + offset

    # 칸의 위치 (행, 열)로 칸의 번호를 계산하는 메소드
    def get_index_by_position(self, r: int, c: int) -> int:
        return (r - 1) * 9 + c


T = int(input())
sudoku = SudokuBoard()
for i in range(T):
    print('Case #%d:' % (i + 1))
    index = int(input())
    r = sudoku.get_row_by_index(index)
    c = sudoku.get_col_by_index(index)
    g = sudoku.get_group_by_index(index)
    print(r, c, g)
