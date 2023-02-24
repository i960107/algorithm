from typing import List


def solution(N: int, M: int, lectures: List[int]) -> int:
    # 한 파일에 몰빵할 경우의 파일 길이
    left, right = 1, max(lectures) * N
    answer = right
    while left <= right:
        mid = left + (right - left) // 2
        if get_required_files(mid, lectures) <= M:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


def get_required_files(length: int, lectures: List[int]) -> int:
    # 여기가 왜 문제지?
    # lecture > length인 경우에는 불가능한 경우로 count 해야 함.
    cnt = 1
    curr_file_length = 0
    for lecture in lectures:
        if curr_file_length + lecture <= length:
            curr_file_length += lecture
        elif lecture <= length:
            cnt += 1
            curr_file_length = lecture
        else:
            # 어떤 강의가 그 자체로 블루레이 크기를 초과하는 경우 무조건 M보다 큰 값을 반환
            cnt = 1000001
            break
    return cnt


N, M = map(int, input().split())
lectures = list(map(int, input().split()))
print(solution(N, M, lectures))
