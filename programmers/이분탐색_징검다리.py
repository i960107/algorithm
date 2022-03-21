def solution(distance: int, rocks: list, n: int) -> int:
    # distance 제한 조건이 1,000,000,000으로 매우 크기때문에 이분탐색 필요하다는것 알 수 있음
    # 이분 탐색을 하려면 정렬되어있어야하고, 시작-끝 범위가 분명해야 한다.
    # 바위들 사이 간격은 최대 distance-1
    # left-mid 구간을 선택할지 mid-right구간을 선택할지 고르는 기준은?
    answer = 0
    # 각 바위 사이 거리의 최솟값
    left = 0
    # 각 바위 사이 거리의 최댓값
    right = distance

    # O(N)
    rocks.sort()
    distances = []
    for i in range(len(rocks)):
        distances.append(rocks[i] - rocks[i - 1] if i != 0 else rocks[i])
    print(distances)

    while left < right:
        pass
    return answer


def solution_others(distance: int, rocks: list, n: int) -> int:
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        min_distance = float('inf')
        curr = 0
        remove_cnt = 0

        for rock in rocks:
            diff = rock - curr
            if diff < mid:
                remove_cnt += 1
            else:
                curr = rock
                min_distance = min(min_distance, diff)

        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1

    return answer


print(solution_others(25, [2, 15, 11, 21, 17], 2))
