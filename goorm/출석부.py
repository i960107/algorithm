from typing import List, Tuple


def sort_by_name_and_height(arr: List[Tuple[str]]) -> List[Tuple[str]]:
    return sorted(arr, key=lambda x: (x[0], x[1]))


N, k = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(tuple(input().split()))

roll_book = sort_by_name_and_height(arr)
print(*roll_book[k - 1])
