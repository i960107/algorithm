from itertools import product
from collections import defaultdict


#
# def solution(n: int, number: int) -> int:
#     if n == number:
#         return 1
#     # 한번 사용해서 만들수 있는 수
#     # replace function call with set literal
#     # parts = [{n}]
#     parts = []
#     for i in range(8):
#         # 전체에 대해 set가 아니라 i개를 사용해 만든 집합에 대해 중복제거? 매 부분해엗 ㅐ해서만 중복이 없으면 됨.
#         # set은 순서가 없기때문에 입력된 순서대로 저장되는 것 아님. 내부적으로 해시
#         part = set()
#         if i >= 1:
#             # 이거 아님!!
#             # part.add(n * 11 * i)
#             part.add(int(str(n) * (i + 1)))
#         else:
#             part.add(n)
#         # 1부터 n-1까지 부분해 조합해서 만들 수 있는 수
#         for j in range(i):
#             for x, y in product(parts[j], parts[i - 1 - j]):
#                 if x + y != number:
#                     part.add(x + y)
#                 else:
#                     return i + 1
#
#                 if x - y != number:
#                     part.add(x - y)
#                 else:
#                     return i + 1
#
#                 if x * y != number:
#                     part.add(x * y)
#                 else:
#                     return i + 1
#
#                 if y != 0 and x // y != number:
#                     part.add(x // y)
#                 elif y != 0 and x // y == number:
#                     return i + 1
#
#         parts.append(part)
#         print(f'parts{i} {len(part)}')
#     return -1
#
#
# def solution_others(n: int, number: int) -> int:
#     answer = 0
#
#     s = [{int(str(n) * (i + 1))} for i in range(8)]
#
#     for i in range(len(s)):
#         # 전체에 대해 Set혹은 i개를 사용해 만든 집합에 대해 중복제거?
#         # 1부터 n-1까지 부분해 조합해서 만들 수 있는 수
#         for j in range(i):
#             for op1 in s[j]:
#                 for op2 in s[i - j - 1]:
#                     # 덧셈과 곱셈은 앞뒤 순서 바뀌어도 같음.
#                     # j의 반까지만 순환하고 뺄셈,나눗셈에 대해서만 앞뒤 순서 바꾸어서 진행해도 되지만
#                     # 얻을게 많지 않고 되려 코드가 복잡해질 수 있으므로 약간의 효율성 희생하더라도 전체 돌기.
#                     # 연산을 진행하면서 nubmer가 같으면 break할 수 있지만 또한, 코드 단순화 택함
#                     s[i].add(op1 + op2)
#                     s[i].add(op1 - op2)
#                     s[i].add(op1 * op2)
#                     if op2 != 0:
#                         s[i].add(op1 // op2)
#
#         if number in s[i]:
#             answer = i + 1
#             break
#         print(f'parts{i} {len(s[i])}')
#     else:
#         answer = -1
#     return answer
#
#
# # print(solution(5, 12))
# print(solution(5, 31168))
# # print(solution(2, 11))
#
# # print(solution_others(5, 12))
# print(solution_others(5, 31168))
#
#
# # print(solution_others(2, 11))


# def solution(N: int, number: int) -> int:
#     # N을 사용한 횟수 : 만들 수 있는 숫자 set
#     d = defaultdict(set)
#     d[0] = {0}
#
#     for prev_cnt in range(0, 8):
#         s = set()
#         if N * int("1" * (prev_cnt + 1)) == number:
#             return prev_cnt + 1
#         s.add(N * int("1" * (prev_cnt + 1)))
#
#         for num in d[prev_cnt]:
#
#             if num + N == number:
#                 return prev_cnt + 1
#             s.add(num + N)
#
#             if num - N == number:
#                 return prev_cnt + 1
#             s.add(num - N)
#
#             if num * N == number:
#                 return prev_cnt + 1
#             s.add(num * N)
#
#             if num // N == number:
#                 return prev_cnt + 1
#             s.add(num // N)
#
#         d[prev_cnt + 1] = s
#         print(prev_cnt + 1, d[prev_cnt + 1])
#
#     return -1


def solution(N: int, number: int) -> int:
    d = dict()
    for cnt in range(1, 9):
        s = set()
        repeated = int(str(N) * cnt)
        if repeated == number:
            return cnt
        s.add(repeated)

        for i in range(1, cnt // 2 + 1):
            for a in d[i]:
                for b in d[cnt - i]:
                    s.add(a + b)
                    s.add(a - b)
                    s.add(b - a)
                    s.add(a * b)
                    if b != 0:
                        s.add(a // b)
                    if a != 0:
                        s.add(b // a)

        if number in s:
            return cnt
        d[cnt] = s
    return -1


print(solution(5, 12))
print(solution(2, 11))
