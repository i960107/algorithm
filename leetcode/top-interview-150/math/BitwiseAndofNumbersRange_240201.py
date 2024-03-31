from typing import List


class Solution:
    def rangeBitwiseAndFail(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        if left == right:
            return left

        def helper(n: int):
            num = 1
            count = 0
            while num * 2 <= n:
                count += 1
                num = num * 2
            return count

        # 같은 구간에 있을때만 1 생김.
        left_result = helper(left)
        right_result = helper(right)
        return 2 ** left_result if left_result == right_result else 0

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if len(bin(left)) != len(bin(right)):
            return 0

        result = right
        # 왜 TimeLimitExceed
        # 직접 -1한 후 & 하면 매번 전체 bit에 대해서 & 연산 실행됨.
        # x &= (x-1)
        # 내부적으로 하면 prefix제외하고 실행됨. 더빠름.
        while right > left:
            right -= 1
            result &= right
        return result


s = Solution()
# print(s.rangeBitwiseAnd(5, 7))
# print(s.rangeBitwiseAnd(1, 2147483647))
# print(s.rangeBitwiseAnd(7, 12))
# print(s.rangeBitwiseAnd(1, 1))
# print(s.rangeBitwiseAnd(1, 0))
# print(s.rangeBitwiseAnd(3, 12))
print(s.rangeBitwiseAnd(3, 3))
print(s.rangeBitwiseAnd(2, 2))
print(s.rangeBitwiseAnd(0, 0))
print(s.rangeBitwiseAnd(1, 2147483647))
print(s.rangeBitwiseAnd(5, 7))
