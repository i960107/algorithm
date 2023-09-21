from collections import defaultdict


class Solution:
    # 구현..
    def convert1(self, s: str, numRows: int) -> str:
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

        # 정렬된 리스트의 인덱스를 가져오기
        sorted_index = sorted(range(len(groups)), key=lambda i: (groups[i], i))

        start = 0
        result = [[] for _ in range(numRows)]
        while start < len(s):
            for i in range(len(groups)):
                if start + i >= len(s):
                    continue
                result[groups[i]].append(s[start + i])
            start = start + len(groups)

        return ''.join([''.join(x) for x in result])

    # 어렵게 생각하지 말고, 한칸씩 증가했다가 한칸씩 내려옴
    def convert2(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)


s = Solution()
print(s.convert(s="PAYPALISHIRING", numRows=3))
print(s.convert("PAYPALISHIRING", 4))
