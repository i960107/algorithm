from typing import List


def solution(cap: int, n: int, deliveries: List[int], pickups: List[int]) -> int:
    # 이번 배송에서 마지막으로 방문해야 하는 집의 인덱스
    final_house = n - 1

    total_distance = 0

    while final_house >= 0:

        distance = (final_house + 1) * 2

        # 이번 배송에서 전달한 물건, 수거한 물건 수
        delivered = 0
        pickuped = 0

        for i in range(final_house, -1, -1):
            curr_delivered = min(deliveries[i], (cap - delivered))
            delivered += curr_delivered
            deliveries[i] -= curr_delivered

            curr_pickuped = min(pickups[i], (cap - pickuped))
            pickuped += curr_pickuped
            pickups[i] -= curr_pickuped

            if delivered == cap and pickuped == cap:
                break

        total_distance += distance

        while final_house >= 0 and not deliveries[final_house] and not pickups[final_house]:
            final_house -= 1

    return total_distance


# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
# print(solution(4, 5, [1, 0, 3, 1, 0], [0, 3, 0, 4, 0]))
print(solution(4, 5, [0, 0, 0, 0, 0], [0, 0, 0, 0, 50]))
# print(solution())
# print(solution())
