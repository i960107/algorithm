import math
from typing import List


# 0으로 나누는 경우는 없으므로 Divizion By Zero Error는 발생하지 않음
# 중간 연산 결과가 4바이트를 넘지 않음. python 은 long과 int를 구분하지 않기 때문에 상관없지만
# java와 같이 statically typed language의 경우 문제될 수 있음.
# 숫자는 음수가 될 수 잇다. c.isnumeric() -> numeric으로 인식못함.
# truncate toward zero. 양수일때는 a//b 하나라도 음수일때는 -0.5 math.trunc 혹은 int연산 사용하기 int연산이 어떻게 일어나는지 살펴보기.
# int simply removes decimal portion without rounding -> truncate(num, 0)와 같음.
# list나 tuple보다는 set으로
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for c in tokens:
            # if c.isnumeric():
            if c not in operations:
                stack.append(int(c))

            else:
                b = stack.pop()
                a = stack.pop()

                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                elif c == "/":
                    stack.append(int(a / b))
        return stack[-1]


s = Solution()
# print(s.evalRPN(tokens=["2", "1", "+", "3", "*"]))
# print(s.evalRPN(tokens=["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
