import heapq
from collections import defaultdict
from typing import List


# 최대 값 , 최소 값을 모두 관리 해야함..
# 최대힙에서 빼낼때, 최소힙에서는 어떻게 제외하지..
# 테스트 케이스 3 실패.
def solution(operations: List[str]) -> List[int]:
    # 중복 원소 있을 수 있으므로 set은 안됨
    d = defaultdict(int)
    max_heap = []
    min_heap = []

    def pop_min():
        while min_heap:
            value = heapq.heappop(min_heap)
            if d[value] == 0:
                continue
            d[value] -= 1
            break

    def pop_max():
        while max_heap:
            value = -heapq.heappop(max_heap)
            if d[value] == 0:
                continue
            d[value] -= 1
            break

    def push(value: int):
        # 유효성 포함? heapq,와 heapush는 값이 달라야 하므로 하나의 list 공유할 수 없음
        heapq.heappush(min_heap, value)
        heapq.heappush(max_heap, -value)
        d[value] += 1

    for operation in operations:
        op, data = operation.split()
        if op == "I":
            push(int(data))
        if op == "D":
            if not min_heap or not max_heap:
                continue
            if data == "-1":
                pop_min()
            elif data == "1":
                pop_max()
    # 마지막에는 pop하는 거 아니고 조회하는 것임!
    # 하나의 원소만 남은 경우 주의!
    # minheap, maxheap따로 처리해주어야!

    min_element = 0
    while min_heap:
        min_element = heapq.heappop(min_heap)
        if d[min_element] > 0:
            break
        min_element = 0

    max_element = 0
    while max_heap:
        max_element = -heapq.heappop(max_heap)
        if d[min_element] > 0:
            break
        max_element = 0

    # max_element = 0
    # while max_heap:
    #     curr_max_element = -heapq.heappop(max_heap)
    #     if d[curr_max_element] > 0:
    #         max_element = curr_max_element
    #         break

    return [max_element, min_element]

    # sorted_element = sorted([x for x, count in d.items() if count > 0])
    # if not sorted_element:
    #     return [0, 0]
    # else:
    #     return [sorted_element[-1], sorted_element[0]]


def solution2(operations: List[str]) -> List[int]:
    min_heap = []
    max_heap = []

    def push(value: int):
        # 유효성 포함? heapq,와 heapush는 값이 달라야 하므로 하나의 list 공유할 수 없음
        heapq.heappush(min_heap, value)
        heapq.heappush(max_heap, -value)

    def pop_max():
        value = -heapq.heappop(max_heap)
        min_heap.remove(value)
        return value

    def pop_min():
        value = heapq.heappop(min_heap)
        max_heap.remove(-value)
        return value

    for operation in operations:
        op, data = operation.split()
        if op == "I":
            push(int(data))
        if op == "D":
            if min_heap and data == "-1":
                pop_min()
            elif max_heap and data == "1":
                pop_max()

    return [-max_heap[0] if max_heap else 0, min_heap[0] if min_heap else 0]
