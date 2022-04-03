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
