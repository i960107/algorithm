from typing import List


class Solution:
    def getSum(self, a: int, b: int) -> int:
        bits = 32
        MASK = (1 << bits) - 1
        INT_MAX = 1 << (bits - 1) - 1
        # MASK = 0xFFFFFFFF  # bits를 활용해서 표현할 수 있을까?
        # INT_MAX = 0x7FFFFFFF  # bits를 활용해서 표현할 수 있을까?

        # 계산하기 쉽도록 전처리 32비트 수로 만들기.
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0

        # 뒷자리부터 계산하기 가장 윗자리로 shift 올린 후 계산 결과를 다시 shift 내린다.
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            # 전가산기 구현
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry

            sum = Q2 ^ carry
            carry = Q1 | Q3
            result.append(str(sum))

        if carry == 1:
            result.append('1')

        # 초과 자릿수 처리 없어짐. 32비트 앞자리는 없어짐.
        result = int(''.join(result[::-1]), 2) & MASK

        # 음수 처리
        if result > INT_MAX:
            # + 1을 안 해주어도 되나?
            result = ~(result ^ MASK)
        return result

    def getSum2(self, a: int, b: int) -> int:
        bits = 32
        MASK = (1 << bits) - 1
        INT_MAX = 1 << (bits - 1) - 1
        # a는 carry값을 고려하지 않는 a와 b의 합
        # 자리수를 올려가며 carry 값이 담기게.
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) ^ MASK

        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a


s = Solution()
print(s.getSum(1, 2))
