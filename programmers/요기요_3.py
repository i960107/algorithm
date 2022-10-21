from typing import List, Any
from collections import Counter


class LinkedList:
    def __init__(self, start: int, end: int, counter: Any, prev: Any = None, next: Any = None):
        self.start = start
        self.end = end
        self.counter = counter
        self.prev = prev
        self.next = next
        self.has_duplicate = False

        if not counter:
            return

        for v in self.counter.values():
            if v > 1:
                self.has_duplicate = True


def solution(S: str, C: List[int]) -> int:
    initial = LinkedList(0, len(S), Counter(S))
    dummy_head = LinkedList(-1, -1, None, None, initial)
    dummy_tail = LinkedList(-1, -1, None, initial, None)
    initial.prev = dummy_head
    initial.next = dummy_tail

    def has_duplicates() -> bool:
        curr = dummy_head
        while curr:
            if curr.has_duplicate:
                return True
            curr = curr.next

        return False

    def divide_range(partition: int):
        curr = dummy_head

        while curr:
            if partition in range(curr.start, curr.end):
                break
            curr = curr.next

        if partition - curr.start < curr.end - partition:
            left_counter = Counter(S[curr.start:partition])
            right_counter = curr.counter - left_counter
        else:
            right_counter = Counter(S[partition: curr.end])
            left_counter = curr.counter - right_counter

        left = LinkedList(curr.start, partition, left_counter)
        right = LinkedList(partition, curr.end, right_counter)

        curr.prev.next = left
        left.next = right
        left.prev = curr.prev
        right.prev = left
        right.next = curr.next

    if not has_duplicates():
        return 0

    for i, partition in enumerate(C):
        divide_range(partition)

        if not has_duplicates():
            return i + 1

    return -1


# print(solution("aabcba", [1, 3, 2]))
# print(solution("aaa", [1, 2]))
# print(solution("aabcddcb", [3, 5, 1, 4, 7]))
# 만약 처음부터 중복이 없다면
# print(solution("abcd", [1, 2]))
# 만약 가능하지 않다면
# print(solution("aabc", [2]))

# 경계값 테스트
print(solution("aabbccdd", [2, 4, 6]))
print(solution("aabbccd", [1, 3, 5]))
print(solution("abbccd", [2, 4]))
print(solution("abcdd", [4]))
print(solution("aabc", [1]))
print(solution("aabc", [3]))
