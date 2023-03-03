from typing import List


def solution(people: List[int], limit: int) -> int:
    people.sort()
    # 이제 추가해야 하는 사람
    left, right = 0, len(people) - 1
    count = 0
    # 모든 원소가 체크되도록
    while left <= right:
        if left != right and people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        count += 1
    return count


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
