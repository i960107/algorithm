from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = bin(n)
        count = 0
        for i in range(2, len(bin_str)):
            if bin_str[i] == "1":
                count += 1
        return count

    # 2진수 변환 -> 몫이 0 이 될때까지
    def hammingWeight2(self, n: int) -> int:
        count = 0
        while n != 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        return count


s = Solution()
print(s.hammingWeight(0b00000000000000000000000000001011))
print(s.hammingWeight(0b11111111111111111111111111111101))
print(s.hammingWeight2(0b00000000000000000000000000001011))
print(s.hammingWeight2(0b11111111111111111111111111111101))
