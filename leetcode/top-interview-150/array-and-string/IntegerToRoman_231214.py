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

        res = []
        a = 1
        while num:
            num, r = num // 10, num % 10
            print(num, r, a)
            if 1 <= r <= 3:
                res.append(d[a] * r)
            elif r == 4:
                res.append(d[5 * a])
                res.append(d[1 * a])
            elif r == 5:
                res.append(d[r * a])
            elif 6 <= r <= 8:
                res.append(d[a] * (r - 5))
                res.append(d[5 * a])
            elif r == 9:
                res.append(d[10 * a])
                res.append(d[1 * a])

            a *= 10
        return ''.join(res[::-1])

    def intToRoman2(self, num: int) -> str:
        # Creating Dictionary for Lookup
        num_map = {
            1: "I",
            5: "V", 4: "IV",
            10: "X", 9: "IX",
            50: "L", 40: "XL",
            100: "C", 90: "XC",
            500: "D", 400: "CD",
            1000: "M", 900: "CM",
        }

        # Result Variable
        r = ''

        # 큰수부터 greedy하게 더해감.
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num -= n
        return r


s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(1994))
print(s.intToRoman(3909))
