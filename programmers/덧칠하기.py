from typing import List


def solution(n: int, m: int, section: List[int]) -> int:
    # 커버된 구역의 마지막 칸번호
    end = 0
    count = 0
    for section_id in section:
        if section_id <= end:
            continue
        end = (section_id + m - 1)
        count += 1
    return count


print(solution(8, 4, [2, 3, 6]))
