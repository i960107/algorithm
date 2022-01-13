from typing import Sequence, Any


def top_of_hanoi():
    pass


def combination():
    pass


def multiple_of_matrix_improved(n: int, A: Sequence, B: Sequence):
    pass


def multiple_of_matrix(n: int, A: Sequence, B: Sequence):
    multiplied = [[None] * n] * n
    for i in range(n):
        for j in range(n):
            for k in range(n):
                multiplied[i][j] += A[i][k] * B[k][i]
    return multiplied


def insert_sort(arr: Sequence):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        # 앞에 데이터는 다 정렬되어 있으므로, 처음으로 key보다 작거나 같은 값 만나면 그 앞 원소들은 다 key보다 작음.
        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# swap 하는 것 vs 한칸씩 뒤로 밀고 난 후에 한번 값 넣기
# insert_sort와 insert_sort_others 모두 O(n^2)복잡도 가짐.
# 또 처음으로 key보다 작은 값 만나면 그 앞에 값 비교를 멈추기 때문에 최적화된 상태임.
def insert_sort_others(arr: Sequence):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            else:
                break
    return arr


def merge_sort(x: Sequence):
    # base case 정렬이 필요없을때 재귀 호출 중지
    if len(x) < 2:
        return x
    start = 0
    end = len(x)
    middle = (start + end) // 2
    sorted = []
    lower = merge_sort(x[start:middle])
    upper = merge_sort(x[middle:end])
    l = u = 0
    while l <= len(lower) - 1 and u <= len(upper) - 1:
        if lower[l] < upper[u]:
            sorted.append(lower[l])
            l += 1
        else:
            sorted.append(upper[u])
            u += 1
    sorted += lower[l:]
    sorted += upper[u:]
    return sorted


print(insert_sort_others([11, 10, 9, 8, 7, 7, 5, 4, 3, 2]))
print(insert_sort([11, 10, 9, 8, 7, 7, 5, 4, 3, 2]))
print(merge_sort([11, 10, 9, 8, 7, 7, 5, 4, 3, 2]))
