from math import sqrt
from itertools import permutations


def solution(brown: int, yellow: int) -> list:
    answer = []
    total = brown + yellow
    divisor = get_divisor(total)

    for height, width in divisor:

        if width < 3 or height < 3:
            continue

        b = (width * 2) + (height - 2) * 2
        y = total - b

        if b == brown and y == yellow:
            answer = [width, height]
            break

    return answer


def get_divisor(num: int):
    divisor = []
    k = int(sqrt(num))
    for x in range(1, k + 1):
        if num % x == 0:
            divisor.append((x, int(num / x)))
    return divisor


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
