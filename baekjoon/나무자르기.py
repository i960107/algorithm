from typing import List


def solution(N: int, M: int, trees: List[int]) -> int:
    left, right = 0, max(trees)
    answer = 0

    while left <= right:
        mid = left + (right - left) // 2

        cut = 0
        # 왜 시간 초과나지? 시간 복잡도가 간당간당할때 사소한 연산 차이로 통과 안될수도.
        # max 연산 효율 안 좋은
        # 비교하지 말고, 무조건 더해주는게 나음듯.
        for tree in trees:
            cut += tree - mid if tree > mid else 0

        # 높이가 정확히 h가 되었을때 안 멈추면 시간 초과?
        if cut < M:
            right = mid - 1

        elif cut >= M:
            answer = mid
            left = mid + 1

    return answer


N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(solution(N, M, trees))
