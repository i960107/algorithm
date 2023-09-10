from typing import List


class Solution:
    def romanToInt2(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        for i in range(1, len(s)):
            curr = d[s[i]]
            prev = d[s[i - 1]]
            if curr > prev:
                total -= prev
            else:
                total += prev
        total += d[s[-1]]
        return total

    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        index = 0
        while index < len(s):
            curr = d[s[index]]
            next = d[s[index + 1]] if index + 1 < len(s) else 0
            if curr >= next:
                total += curr
                index += 1
            else:
                total -= curr
                total += next
                index += 2
        return total


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("M"))
print(s.romanToInt("MCMXCIV"))
print(s.romanToInt("LVIII"))
