import heapq
from typing import List


def solution(arr: List[int], k: int) -> int:
    heapq.heapify(arr)

    # 9개 중 4번째로 큰 원소 -> 6번째 작은 원소
    for _ in range(len(arr) - k):
        heapq.heappop(arr)

    return heapq.heappop(arr)


def solution2(arr: List[int], k: int) -> int:
    # O(NLogN))
    # heap = heapq.heapify([-x for x in arr])

    # O(NlogN)
    heap = list()
    for x in arr:
        heapq.heappush(heap, (-x, x))

    answer = None
    for _ in range(k):
        answer = heapq.heappop(heap)[1]
    return answer


def solution3(arr: List[int], k: int) -> int:
    '''heapq모듈의 nlargest이용'''
    # O(NlogN)
    return heapq.nlargest(k, arr)[-1]


def solution4(arr: List[int], k: int) -> int:
    '''정렬을 이용한 풀이'''
    # 추가 삭제가 빈번할때는 힙 정렬이 유용하지만, 입력값이 고정되어 있는 경우 한번 정렬하는게 좋음

    # arr.sort()
    # return arr[-k]

    # 정렬후
    arr.sort(reverse=True)
    # k번째 값 추출
    return arr[k - 1]


print(solution([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(solution2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(solution3([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(solution4([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
