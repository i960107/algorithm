from typing import List


def solution(food_time: List[int], k: int) -> int:
    min_food_time = 1001
    for time in food_time:
        if time < min_food_time:
            min_food_time = time

    n = len(food_time)
    while k > 0:
        eat = k // n if k // n > min_food_amount else


print(solution([3, 1, 2], 5))
