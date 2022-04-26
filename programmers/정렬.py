from typing import List, Optional


def bubble_sort(array: List[int]) -> List[int]:
    # 상관 없음? len(array)까지 비교해서 j범위 없어서 for문 안 들어가지 않음
    # for i in range(len(array) ):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def bubble_sort2(array: List[int]) -> List[int]:
    # 최적화 되지 않은 버전. 이미 정렬된 부분 계속 재정
    for i in range(1, len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print(bubble_sort2([3, 2, 1, 9, 4]))
print(bubble_sort2([3, 2, 1, 9, 4]))


def merge_sort(arr: List[int]) -> Optional[List[int]]:
    # 최선과 최악 모두 O(NlogN)인 알고리즘. 안정 정렬, 일정한 실행 속도, 고른 성능
    # 안정 정렬 알고리즘은 중복된 값을 입력 순서와 동일하게 정렬한다.
    # 재정렬하면 기존 순서가 그대로 유지된 상태에서 정렬이 이뤄짐

    # 왜안되지?
    # 빈 배열일때만 처리해주면 안됨!
    # 원소의 개수가 하나일때 계속 나누면 maximum recursive call error 발생
    # if not arr:
    #     return None
    if len(arr) <= 1:
        return arr

    # divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # conquer
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            # 배열 + 빈 배열 = 원래 배열, 빈 배열 원소 없는 것!
    # append 아니고 concat임! 주의!
    result += left[i:]
    result += right[j:]
    return result


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))


def quick_sort(arr: List[int], lo: int, hi: int) -> Optional[List[int]]:
    '''피벗을 기준으로 좌우 나누는 파티션 교환 정렬. 분할 정복 알고리즘'''

    # O(NlogN). 재귀호출 LogN번. 매 호출마다 탐색하는 범위 N
    # 최악의 경우 O(N^2)알고리즘. 이미 정렬된 배열이 입력값으로 들어오면 파티셔닝이 전혀 이뤄지지 않는다
    # 이때 n번의 라운드에 걸쳐 전체를 비교하기 때문에 최악의 성능을 보이게 된다.
    # 불안정 정렬 : 기존 정렬 순서는 무시된 채 섞임

    # 수도 코드
    # if lo < hi then
    # pivot := partition(A, lo, hi)
    # pivot 포함하지 않고 정렬
    # Quicksort(A, lo, pivot -1)
    # Quicksort(A, pivot+1, hi)
    def partition(A: List[int], lo: int, hi: int) -> int:
        '''퀵 소트의 가장 간단한 분할 알고리즘인 로무토 파티션'''
        # 맨 오른쪽을 피벗으로 정하는 가장 단순한 방식
        # 맨오른쪽 값을 기준으로, 2개의 포인터가 이동해서 오른쪽 포인터의 값이 피벗보다 작다면 서로 스왑하는 형태
        pivot = A[hi]
        left = lo
        # 오른쪽 포인터가 끝에 즉 hi-1에 도달하게 되면
        # left 포인터 왼쪽에 피벗보다 작은 값 오른쪽에 피벗보다 큰 값이 위치하게 된다.
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    # 분할하면서 정복을 진행하여 코드 기준으로 Lo < hi를 만족하지 않을때까지,
    # 즉, 서로 위치가 역전할때까지 계속 재귀로 반복하면서 정렬이 완료
    # lo = p 혹은 hi = p 인경우 역전
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot - 1)
        quick_sort(arr, pivot + 1, hi)

    return arr

# 파이썬의 기본 알고리즘 : 실무에서는 안정 정렬이자 고른 성능인 병합 정렬이 활발하게 쓰이고 있으며, 파이썬의 기본 정렬 알고리즘으로는
# 병합 정렬과 삽입 정렬이 휴리스틱하게 조합된 팀소트를 사용
