from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    def dfs(row: int, column: int):
        # 원래 픽셀이 newColor였어도 그 인접행렬 탐색해야 하지 않나?
        # if image[row][column] == newColor:
        #     return
        if image[row][column] != color:
            return
        image[row][column] = newColor
        if row - 1 >= 0:
            dfs(row - 1, column)
        if row + 1 < len(image):
            dfs(row + 1, column)
        if column - 1 >= 0:
            dfs(row, column - 1)
        if column + 1 < len(image[row]):
            dfs(row, column + 1)

    color = image[sr][sc]
    if color == newColor:
        return image
    dfs(sr, sc)
    return image


# 왜 에러나지?
print(floodFill(image=[[0, 0, 0], [0, 1, 1]], sr=1, sc=1, newColor=1))
print(floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
print(floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, newColor=2))
