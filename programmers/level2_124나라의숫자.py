from math import log

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


def solution_124_country(n: int) -> Tuple[int, int]:


    return group, order


for i in range(1, 50):
    print(f'{i} : {solution_124_country(i)}')
