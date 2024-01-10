from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pattern = []
        for i in range(numRows):
            pattern.append(i)
        for i in range(numRows - 2, 0, -1):
            pattern.append(i)

        result = [[] for _ in range(numRows)]
        for i, c in enumerate(s):
            result[pattern[i % len(pattern)]].append(c)

        answer = ""
        for res in result:
            answer += ''.join(res)
        return answer


s = Solution()
print(s.convert(s="PAYPALISHIRING", numRows=3))
print(s.convert(s="PAYPALISHIRING", numRows=4))
print(s.convert(s="PAYPALISHIRING", numRows=5))
print(s.convert(s="PAYPALISHIRING", numRows=6))
