from typing import List


def solution(strArr: List[str]):
    def convert_to_2d_list(strArr: List[str]) -> List[List[str]]:
        arr = []
        for s in strArr:
            arr.append(s[1:-1].split(","))
        return arr

    arr = convert_to_2d_list(strArr)

    def is_upward(i: int, j: int) -> bool:
        return (i + j) % 2 == 0

    def is_top_end(i: int, j: int) -> bool:
        return i == 0 and j % 2 == 0

    def is_bottom_end(i: int, j: int) -> bool:
        if j != 0 and i != m - 1:
            return False
        return True

    m, n = len(arr), len(arr[0])
    i, j = 0, 0

    answer = []
    while i < m and j < n:
        print(i, j, arr[i][j])
        answer.append(arr[i][j])
        if is_top_end(i, j):
            j += 1
            continue
        if is_bottom_end(i, j):
            if is_upward(i, j):
                i -= 1
                j += 1
                continue
            if j == 0 and i < m - 1:
                i += 1
            else:
                j += 1
            continue
        if is_upward(i, j):
            i -= 1
            j += 1
        else:
            i += 1
            j -= 1

    return answer


print(solution(["[1, 2, 3, 4, 5]", "[6, 7, 8, 9, 10]", "[11, 12, 13, 14, 15]"]))
