from typing import List


class Solution:
    # brute force
    def trailingZeroes(self, n: int):
        def _factorial(num: int):
            if num <= 1:
                return num

            return num * _factorial(num - 1)

        res = _factorial(n)
        zeroes = 0
        while res > 0 and res % 10 == 0:
            zeroes += 1
            res = res // 10
        return zeroes

    # 수학적인 intuition
    # O(LogN)
    def trailingZeroesFaster(self, n: int):
        ans = 0
        # 1 ~ n까지 숫자들의 약수 중 5의 개수
        # 125의 경우 5의배수들이 1개, 25의 배수들이 2개씩 가지고 있음
        t = n // 5
        while t > 0:
            ans += t
            t //= 5
        return ans


s = Solution()
print(s.trailingZeroes(5))
print(s.trailingZeroes(0))
print(s.trailingZeroes(3))
