from typing import List


def solution(n: int, times: list) -> int:
    sec = 0
    # 입국심사관별 작업 들어간 시간. 비어있으면 0
    examiners = [0] * len(times)
    while True:
        for i, x in enumerate(zip(examiners, times)):
            if sec - x[0] >= x[1]:
                examiners[i] = 0
        break

    return sec


def solution_others(n: int, times: list) -> int:
    answer = 0
    left = 1
    # 최장시간 걸리는 경우 : 가장 오래 걸리는 심사관이 모든 사람을 심사
    right = max(times) * n
    while left < right:
        mid = (left + right) // 2
        total = 0

        # 특정시간동안 모든 작업대에서 처리할 수 있는 사람 수
        for t in times:
            total += mid // t
        # 처리해야하는 사람 수 보다 더 많은 사람을 처리할 수 있다면
        # -> 더 적은 시간에 모든 사람 처리할 수 있음
        # 같다면?
        if total >= n:
            # total >=n 이므로 total= n일수도 있음. left= mid
            right = mid
        else:
            # total < n 이므로 mid보다 큰 부분이 탐색 대상. left =mid+1
            left = mid + 1
    # 왜 right 아닌 left지?
    answer = left

    return answer


print(solution_others(6, [7, 10]))


# set1 = set([1, 2, 2, 1]) set2 = set([2, 2])
# print(set1.intersection(set2))

def solution_practice(n: int, times: List[int]) -> int:
    times.sort()
    # left를 다음과 같이 지정할경우 times = [7, 14]일때 부정확한 값이 됨.
    # 실제로 구하려면 time의 최소 공배수와 각 time의 나눗셈 결과를 해야함.
    # left, right = times[-1] * n // len(times), times[-1] * n
    # 조건을 만족하는 최소값
    left, right = 0, times[-1] * n
    answer = right
    while left <= right:
        mid = left + (right - left) // 2
        # 이 시간안에 다 처리할 수 있으면:
        # 각 심사관이 쉬지 않고 심사했을때 처리할 수 있는 사람 수, 최대로 처리 가능한 경우이기 때문에
        # n이 이것보다 작다면, 처리할 수 있음
        # 가장 짧게 걸리는 사람이 가장 많이 처리하는게 가장 효율적.
        max_immigration = 0
        for time in times:
            max_immigration += mid // time
        if n <= max_immigration:
            right = mid - 1
            answer = min(answer, mid)
        # 이 시간안에 다 처리할 수 없으면:
        else:
            left = mid + 1
    return answer


print(solution_practice(6, [7, 10]))
