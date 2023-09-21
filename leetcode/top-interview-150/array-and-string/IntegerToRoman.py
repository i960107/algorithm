from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        multiple = 1
        result = []
        while num > 0:
            n = num % 10
            if n * multiple in d:
                result.append(d[n * multiple])
            # 2,3 or 6,7,8
            elif n % 5 <= 3:
                result.append((d[5 * multiple] if n > 5 else '') + d[multiple] * (n % 5))
            # 4  or 9
            elif n % 5 == 4:
                result.append(d[multiple] + (d[10 * multiple] if n > 5 else d[5 * multiple]))

            num //= 10
            multiple *= 10
        return ''.join(result[::-1])

    # 4, 9 계열만 딕셔너리에 추가해줘도..
    def intToRoman2(self, num: int) -> str:
        num_map = {
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
            1000: "M"
        }
        # 400부터는 없음

        r = ''
        for n in num_map:
            while n <= num:
                r += num_map[n]
                num -= n
        return r


s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(58))
print(s.intToRoman(1994))
