import copy
from typing import List, Final

'''스도쿠 보드 채우기'''


class Sudoku:
    EMPTY: Final = 0

    def __init__(self):
        self.board = [[0] * 10 for _ in range(10)]
        self.row_frequency = [[0] * 10 for _ in range(10)]
        self.column_frequency = [[0] * 10 for _ in range(10)]
        self.group_frequency = [[0] * 10 for _ in range(10)]

    def set_board(self, r: int, c: int, value: int):
        self.clear_board(r, c)

        g = ((r - 1) // 3) * 3 + (c - 1) // 3 + 1

        self.row_frequency[r][value] += 1
        self.row_frequency[c][value] += 1
        self.row_frequency[g][value] += 1

        self.board[r][c] = value

    def clear_board(self, r: int, c: int):
        if self.board[r][c] == self.EMPTY:
            return

        value = self.board[r][c]
        g = ((r - 1) // 3) * 3 + (c - 1) // 3 + 1

        self.row_frequency[r][value] -= 1
        self.row_frequency[c][value] -= 1
        self.row_frequency[g][value] -= 1

        self.board[r][c] = self.EMPTY

    def get_board(self, r: int, c: int) -> int:
        return self.board[r][c]

    def is_empty(self, r: int, c: int) -> bool:
        return self.board[r][c] == self.EMPTY

    def is_settable(self, r: int, c: int, value: int):
        if not self.is_empty(r, c):
            return False

        g = ((r - 1) // 3) * 3 + (c - 1) // 3 + 1

        return self.row_frequency[r][value] == 0 \
               and self.column_frequency[c][value] == 0 \
               and self.group_frequency[g][value] == 0

    def copy_board(self) -> List[List[int]]:
        return copy.deepcopy(self.board)


# def fill_sudoku(depth: int, sudoku: Sudoku) -> List[List[int]]:
#     if depth == 81:
#         return sudoku.copy_board()
#
#     result = None
#     for r in range(10):
#         for c in range(10):
#             if not sudoku.is_empty(r, c):
#                 continue
#             for value in range(1, 10):
#                 if not sudoku.is_settable(r, c, value):
#                     continue
#                 sudoku.set_board(r, c, value)
#                 result = fill_sudoku(depth + 1, sudoku)
#                 if result:
#                     break
#                 sudoku.clear_board(r, c)
#     return result


sudoku = Sudoku()
for r in range(10):
    for c, value in enumerate(map(int, input().split())):
        sudoku.set_board(r, c, value)

answer = fill_sudoku(1, sudoku)
for row in answer:
    print(*row)
