from typing import List


def solution_fatigue(k: int, dungeons: List[List]) -> int:
    # 최대 던전의 수!
    dungeons.sort(key=lambda x: x[1])
    # 인덱스 아니고 탐험할 수 있는 던전 수
    # 최소 필요 피로도
    l, u = 0, len(dungeons)
    while l < u:
        mid = l + (u - l) // 2
        # left_fatigue = k - sum(dungeons[0:mid+1][1])
        left_fatigue = k - sum(dungeons[x][1] for x in range(mid))
        if mid + 1 < len(dungeons) and left_fatigue >= dungeons[mid + 1][0]:
            # 아직 다음 던전 탐험할 수 있음
            l = mid + 1
        else:
            # 다음 던전 탐험할 수 없음
            # 현재까지 탐험가능?
            if left_fatigue >= 0:
                return mid
            else:
                u = mid - 1


print(solution_fatigue(80, [[80, 20], [50, 40], [30, 10]]))
