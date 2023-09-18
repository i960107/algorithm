from collections import defaultdict


class Solution:
    # 구현..
    def convert(self, s: str, numRows: int) -> str:
        result = []
        n = len(s)

        d = defaultdict(list)
        groups = [r for r in range(numRows)]
        groups += [r for r in range(numRows - 2, 0, -1)]
        for i, c in enumerate(s):
            group = groups[i % len(groups)]
            d[group].append(c)

        result = ''
        for i in range(numRows):
            result += ''.join(d[i])
        return result

    def convert(self, s: str, numRows: int) -> str:
        groups = [r for r in range(numRows)]
        groups += [r for r in range(numRows - 2, 0, -1)]

        result = []
        for i, n in enumerate(groups):
            result.append((n, i))
        result.sort()
        


s = Solution()
print(s.convert(s="PAYPALISHIRING", numRows=3))
print(s.convert("PAYPALISHIRING", 4))
