from typing import List


# def solution(arr: List[str]) -> int:
#     dp = [{int(arr[0])}]
#     has_subtraction = False
#     for i in range(1, len(arr), 2):
#         s = set()
#         n2 = int(arr[i + 1])
#         op = arr[i]
#
#         if op == "+":
#             for n1 in dp[-1]:
#                 s.add(n1 + n2)
#             if has_subtraction:
#                 s.add(n1 - n2)
#         else:
#             for n1 in dp[-1]:
#                 s.add(n1 - n2)
#                 if has_subtraction:
#                     s.add(n1 + n2)
#             has_subtraction = True
#
#         dp.append(s)
#
#     print(dp)
#     return max(dp[-1])

# def solution(arr: List[str]) -> int:
#     dp = [{0}]
#
#     for i in range(len(arr) - 2, 0, -2):
#
#         if arr[i] == "+":
#             s = set()
#             for x in dp[-1]:
#                 s.add(int(arr[i + 1]) + x)
#             dp.append(s)
#         else:
#             s = set()
#             for x in dp[-1]:
#                 s.add(- int(arr[i + 1]) + x)
#                 s.add(- int(arr[i + 1]) - x)
#             dp.append(s)
#
#     answer = -1 * 1000 * 101 - 1
#     print(dp)
#     for x in dp[-1]:
#         answer = max(x + int(arr[0]), answer)
#
#     return max(dp[-1])
#


def solution(arr:List[str]) -> int:
    pass
print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
