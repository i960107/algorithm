from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        # row
        for row in board:
            num_set = set()
            for curr in row:
                if curr == ".":
                    continue
                if curr in num_set:
                    return False
                num_set.add(curr)

        # column
        for c in range(n):
            num_set = set()
            for r in range(n):
                curr = board[r][c]
                if curr == ".":
                    continue
                if curr in num_set:
                    return False
                num_set.add(curr)

        # subbox
        # i, j = 0, 0
        # while i < n:
        #     num_set = set()
        #     for r in range(i, i + 3):
        #         for c in range(j, j + 3):
        #             curr = board[r][c]
        #             if curr == ".":
        #                 continue
        #             if curr in num_set:
        #                 return False
        #             num_set.add(curr)
        #     if j + 3 >= n:
        #         i += 3
        #         j = 0
        #     else:
        #         j += 3
        sub_box_set = set()
        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                curr = (r // 3, c // 3, board[r][c])
                if curr in sub_box_set:
                    return False
                sub_box_set.add(curr)
        return True

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        n = len(board)
        element_set = set()
        for r in range(n):
            for c in range(n):
                curr = board[r][c]
                if curr == ".":
                    continue
                # board[5][4] = 4, board[4][5] = 5인경우인경우?
                # String vs int
                # r 0 ~ 8 c 0 ~8 curr 1 ~ 9
                for e in [(r, curr), (curr, c), (r // 3, c // 3, curr)]:
                    if e in element_set:
                        return False
                    element_set.add(e)

        return True


s = Solution()
print(s.isValidSudoku(board=
                      [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                          , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                          , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                          , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                          , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                          , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                          , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                          , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                          , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
