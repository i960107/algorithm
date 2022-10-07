from typing import List, Final


class Quilting:
    EMPTY: Final = -1

    def __init__(self, h: int, w: int, imageA: List[List[int]], imageB: List[List[int]]):
        self.h = h
        self.w = w
        self.imageA = imageA
        self.imageB = imageB
        self.memo = [[self.EMPTY] * w for _ in range(h)]

    def get_min_color_difference(self, last_row: int, last_col: int) -> int:

        if last_row < 0 or last_row >= h or last_col < 0 or last_col >= w:
            return 255 ** 2 + 1

        elif self.memo[last_row][last_col] != self.EMPTY:
            return self.memo[last_row][last_col]

        if last_row == 0:
            answer = (self.imageA[last_row][last_col] - self.imageB[last_row][last_col]) ** 2
        else:
            answer = min(self.get_min_color_difference(last_row - 1, last_col - 1),
                         self.get_min_color_difference(last_row - 1, last_col),
                         self.get_min_color_difference(last_row - 1, last_col + 1)) \
                     + (self.imageA[last_row][last_col] - self.imageB[last_row][last_col]) ** 2

        self.memo[last_row][last_col] = answer

        return answer


h, w = map(int, input().split())

imageA = []
for _ in range(h):
    imageA.append(list(map(int, input().split())))

imageB = []
for _ in range(h):
    imageB.append(list(map(int, input().split())))

q = Quilting(h, w, imageA, imageB)

answer = float('INF')
for col in range(w):
    answer = min(answer, q.get_min_color_difference(h-1, col))
print(answer)
