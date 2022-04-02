from math import log
from math import ceil

from typing import Tuple


# def solution_124_country(n: int) -> str:
#     '''124나라의 숫자'''
#     orders = ['4', '1', '2']  # 3개값이 번갈아가며 나오는데 % 3 나머지가 인덱스
#     answer = ''
#     if n <= 3:
#         answer = orders[(n) % 3]
#     # else:
#     #     n, order = n // 3, n % 3
#     #     answer += orders[order]
#     else:
#         group, order = n // 3, n % 3
#         answer += orders[order]
#
#         if group > 3:
#             group -= 1
#             while group > 3:
#                 group, order = n // 3, n % 3
#                 answer += orders[order]
#             answer += orders[group]
#         else:
#             answer += orders[group % 3]
#
#         while n > 3:
#             n, order = (n - 1) // 3, (n - 1) % 3
#             answer += orders[order]
#         answer += orders[n]
#
#     return answer[::-1]


def solution_124_country(n: int) -> int:
    answer = ''
    i = 0
    length = 3 ** i
    border = 0
    numbers = [1, 2, 4]

    while True:
        if border + 3 ** (i + 1) >= n:
            break
        i += 1
        length += 1
        border += 3 ** i

    while length > 0:
        idx = ((n - border) // 3 ** (length - 1)) % 3
        if length != 1:
            answer += str(numbers[idx])
        else:
            answer += str(numbers[idx - 1])
        length -= 1

    return int(answer)


def solution_124_country_others(n: int) -> str:
    if n <= 3:
        return '124'[n - 1]
    else:
        q, r = divmod(n - 1, 3)
        return solution_124_country_others(q) + '124'[r]


def solution_124_country_others2(n: int) -> str:
    answer = ''
    while n > 0:
        n -= 1
        n, remainder = divmod(n, 3)
        answer += '124'[remainder]
    return answer[::-1]


for i in range(1, 50):
    print(f'{i} : {solution_124_country_others2(i)}')
