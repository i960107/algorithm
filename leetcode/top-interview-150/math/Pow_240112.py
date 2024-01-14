from functools import cache
from typing import List


class Solution:
    def myPow_fail(self, x: float, n: int) -> float:
        if not x:
            return x

        # n = -1인 경우
        if n < 0:
            x = 1 / x
            n = -n

        # n = 0인 경우
        if n == 0:
            return 1

        # 어디서 로그를 찍는게 좋을까?
        # n, temp_pow  -> res, x
        # 전체 값 바뀌는 걸 추적하고 싶다면 시작하기 전, 값이 모두 변경되고 난 후.
        # 중간에 추적한다면 temp_pow값이 갱신되지 않거나, temp_pow에 의해서 처리된 값을 추적하기 어려움.
        res = x
        while n > 1:
            print(x, n)
            temp_pow = 1
            for i in range(2, n + 1):
                if n % i == 0:
                    n = n // i
                    temp_pow = i
                    break

            temp = 1
            for _ in range(temp_pow):
                temp *= x
            res = temp
            x = res
        return res

    # x 가 0인 경우는?
    # @cache, from functools import cache -> dp의 memoization에서 subproblem들의 return값을 기억해두는 것
    # @cache -> python3.9부터 사용가능
    # memoization은 재귀적으로 처리하는게 가장 빠름.
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == - 1:
            return 1 / x
        return self.myPow(x, n // 2) * self.myPow(x, n // 2) * self.myPow(x, n % 2)


s = Solution()
# print(s.myPow(2.0, -2))
# print(s.myPow(2.0, 10))
print(s.myPow(0.00001, 2147483647))
