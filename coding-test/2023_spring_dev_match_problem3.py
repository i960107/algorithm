# from typing import List
#
# '''팰린드롬 게임 위너 구하기'''
#
#
# # 하나의 수 1만 뺄 수 있음
# # 정확성 테스트 실패.
def solution(queries: List[List[int]]) -> List[int]:
    pass


def dfs(query: List[int]) -> List[int]:
    count = 0
    stack = []
    stack.append((query, 0))
    visited = set()
    while stack:
        curr = stack.pop()
        if

    pass


def is_palindrome(queyr: List[int]) -> bool:
    n = len(queyr)
    count = 0
    for index in range(n // 2):
        pair_index = n - 1 - index
        if queyr[index] != queyr[pair_index]:
            return False
    return True

# def solution(queries: List[List[int]]) -> List[int]:
#     answer = []
#     for query in queries:
#         winnable = False
#         turn = get_required_count_to_make_palindrome(query)
#         if turn % 2 == 1:
#             answer.append(1)
#             continue
#         for index, x in enumerate(query):
#             if x != 0:
#                 temp = query.copy()
#                 temp[index] = x - 1
#                 turn = get_required_count_to_make_palindrome(temp)
#                 turn -= 1
#                 player = 1 if turn % 2 == 1 else 2
#                 if player == 1:
#                     winnable = True
#                     break
#         answer.append(int(winnable))
#     return answer
#
#
# def get_required_count_to_make_palindrome(query: List[int]) -> int:
#     n = len(query)
#     count = 0
#     for index in range(n // 2):
#         pair_index = n - 1 - index
#         count += abs(query[index] - query[pair_index])
#     return count
#
#
# print(solution([[2, 0], [3, 1]]))
# print(solution([[1, 4, 3], [1, 2, 2]]))
# # print(solution([[0, 2, 0, 1], [0, 1, 0, 1]]))
# # print(solution([[0, 9], [1, 9, 8, 0]]))
# # print(solution([[1, 9, 8, 0, 1]]))
# # print(solution([[1, 1, 3], [9, 0, 0], [1, 0, 2, 4]]))
# print(solution([[9, 0, 0]]))
