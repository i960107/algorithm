from typing import List
from collections import deque


def sliding_window_maximum_brute_force(nums: List[int], k: int) -> List[int]:
    '''브루트 포스로 계산 '''
    # 배열의 길이 8 윈도우 크기 3 -> 결과 배열 6개
    if not nums:
        return nums
    r = []
    # 전체 복잡도 O(k*N)
    # O(N)
    for i in range(len(nums) - k + 1):
        # 가장 큰 원소 담기
        # O(k)
        r.append(max(nums[i:i + k]))
    return r


def sliding_window_maximum_queue(nums: List[int], k: int) -> List[int]:
    '''큐를 이용한 최적화'''
    # 필요할때만 max()를 계산. 최댓값 계산을 최소화
    results = []
    window = deque()

    # 왜 sys.min() 안하고 float형으로 지정하지? 상관 없음
    # 시스템에서 지정할 수 있는 가장 낮은 값
    current_max = float('-inf')

    for i, v in enumerate(nums):
        window.append(v)

        if i < k - 1:
            continue

        # 새로 추가된 값이 기존 최대값보다 큰 경우 교체
        # 최댓값이 윈도우에서 빠진 경우에만 윈도우안 원소들 중 최댓값 탐색
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)

        # 신규 요소 추가 전 앞 요소 빠지기
        # 최댓값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = float('-inf')
    return results


print(sliding_window_maximum_brute_force([1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(sliding_window_maximum_queue([1, 3, -1, -3, 5, 3, 6, 7], k=3))
