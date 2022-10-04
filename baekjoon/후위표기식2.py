import math
import sys
import operator
from typing import List


def solution():
    input = sys.stdin.readline
    count = int(input())
    # dict형 아니고 배열로 저장해도됨.
    # 들어온 숫자 순서가 인덱스를 가리키므로
    nums = dict()

    post_notation = input().rstrip()
    for i in range(count):
        nums[chr(ord("A") + i)] = input().rstrip()

    print(nums)
    stk = []

    for char in post_notation:
        if char not in "+-*/":
            # int로 변환하지 않을 경우 무조건 rstrip()필요
            stk.append(nums[char])
        else:
            b = stk.pop()
            a = stk.pop()
            stk.append(str(eval(a + char + b)))

    print("{:.2f}".format(stk[0]))


def solution2(expression: str, nums: List[int]) -> str:
    num_d = {}
    for i, num in enumerate(nums):
        num_d[chr(i + 65)] = num

    stk = []
    for x in expression:

        if x.isalpha():
            stk.append(num_d[x])

        else:
            b, a = stk.pop(), stk.pop()
            res = eval(str(a) + x + str(b))
            stk.append(res)

    return f'{stk.pop():.2f}'


res = solution2("ABC*+DE/-", [1, 2, 3, 4, 5])
print(res, res == 6.2)

res = solution2("AA+A+", [1])
print(res, res == 3)
