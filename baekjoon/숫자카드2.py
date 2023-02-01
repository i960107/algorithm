from typing import List
from collections import Counter


def solution_counter(n: int, cards: List[int], m: int, numbers_to_check: List[int]) -> List[int]:
    # O(N) 복잡도를 가짐.
    cards_counter = Counter(cards)
    return [cards_counter[number] for number in numbers_to_check]


def solution_binary_search(n: int, cards: List[int], m: int, numbers_to_check: List[int]) -> List[int]:
    # O(NlogN)복잡도를 가짐.
    cards.sort()
    return [get_count_by_binary_search(target, cards) for target in numbers_to_check]


def get_count_by_binary_search(target: int, numbers: List[int]) -> int:
    # number == target 이라는 조건을 만족하는 인덱스의 최소값, 최대값.
    first = get_first_occurrence(target, numbers, 0, len(numbers) - 1)
    if first == -1:
        return 0
    last = get_last_occurrence(target, numbers, first, len(numbers) - 1)
    return last - first + 1


def get_first_occurrence(target: int, numbers: List[int], lo: int, hi: int) -> int:
    while lo <= hi:
        mid = lo + (hi - lo) // 2

        # 만약 numbers[mid] == target이지만 첫번째가 아닌경우? 어떻게 처리해줘야하나.
        if (mid == 0 or numbers[mid - 1] != target) and numbers[mid] == target:
            return mid
        if numbers[mid] < target:
            lo = mid + 1
        # numbers[mid] == target and numbers[mid-1] == target인 경우 포함.
        else:
            hi = mid - 1
    return -1


def get_last_occurrence(target: int, numbers: List[int], lo: int, hi: int) -> int:
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if (mid == len(numbers) - 1 or numbers[mid + 1] != target) and numbers[mid] == target:
            return mid
        if numbers[mid] <= target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def get_solution_bisect(n: int, cards: List[int], m: int, numbers_to_check: List[int]) -> List[int]:
    answer = []
    cards.sort()
    for num in numbers_to_check:
        left = bisect_left(num, cards)
        if left == n or cards[left] != num:
            answer.append(0)
            continue
        right = bisect_right(num, cards, left, len(cards))
        answer.append(right - left)
    return answer


def bisect_left(target: int, numbers: List[int]) -> int:
    lo, hi = 0, len(numbers)
    while lo < hi:

        mid = lo + (hi - lo) // 2
        # 만약 numbers[lo] ==  target이 된다면 항상 numbers[mid] >= target이므로 lo 포인터는 이동하지 않음.
        if numbers[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    # lo == hi
    return lo


# bisect_right != get_last_index
def bisect_right(target: int, numbers: List[int], lo: int = None, hi: int = None) -> int:
    if lo is None and hi is None:
        lo, hi = 0, len(numbers)

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if numbers[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    # lo == hi
    return lo


n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers_to_check = list(map(int, input().split()))
# print(*solution_counter(n, cards, m, numbers_to_check))
# print(*solution_binary_search(n, cards, m, numbers_to_check))
print(*get_solution_bisect(n, cards, m, numbers_to_check))
