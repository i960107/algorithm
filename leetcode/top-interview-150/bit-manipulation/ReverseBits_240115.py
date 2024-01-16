from typing import List


class Solution:
    # ^bitmask => bitwise not 연산.
    # reverse 아님.
    def reverseBits(self, n: int) -> int:
        # bitmask는 어떻게 만들지 n이 몇자리 수인지 어떻게 알 수 있지
        # 문제 조건 32bits unsigned int
        # 결과가 0000000a처럼 되야함.
        # 그리고 Shift연산으로 마지막 자리 한자리씩 빼가기.
        # & 1하면 안됨.
        # &0000001
        result = 0
        for i in range(4):
            bit = (n >> i) & 1  # 무조건 1이 되지 않나 | 1은 무조건 1이지만 &1은 1일경우 1 아니면 0 임. 그대로
            # result += (bit << (3 - i))
            result |= (bit << (3 - i))
        return result


s = Solution()
print(bin(s.reverseBits(0b0011)))
# print(s.reverseBits(0b00000010100101000001111010011100))
