class Solution:
    # 이것도 이분 탐색이 가능..
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        result = 0
        for n in range(1, x):
            if n * n <= x:
                result = n
            else:
                break
        return result

    def mySqrt2(self, x: int) -> int:
        result = 0
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= x:
                result = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return result


s = Solution()
print(s.mySqrt2(8))
print(s.mySqrt2(4))
print(s.mySqrt2(1))
print(s.mySqrt2(0))
