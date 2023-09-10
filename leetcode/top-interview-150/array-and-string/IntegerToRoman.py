from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        # possible_numbers = dict()
        #
        # for c1, n1 in d.items():
        #     for c2, n2 in d.items():
        #         if n1 > n2:
        #             continue
        #         elif n1 == n2:
        #             possible_numbers[n1] = c1
        #         elif n1 < n2:
        #             possible_numbers[n2 - n1] = c1 + c2
        # 가장 가까운 수를 구해야하나..
        s = str(num)
        print(num)
        for i, c in enumerate(s):
            target = int(c) * (10 ** (len(s) - i - 1))
            print(target)


s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(58))
print(s.intToRoman(1994))
