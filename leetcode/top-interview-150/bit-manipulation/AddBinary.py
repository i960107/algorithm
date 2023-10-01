from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = len(a) if len(a) >= len(b) else len(b)
        a = a.rjust(max_len, "0")[::-1]
        b = b.rjust(max_len, "0")[::-1]

        up = False
        result = []
        print(a, b)
        for x, y in zip(a, b):
            if x == y == "1":
                result.append("0" if not up else "1")
                up = True
            elif x == "1" or y == "1":
                if up:
                    result.append("0")
                    up = True
                else:
                    result.append("1")
                    up = False
            else:
                result.append("1" if up else "0")
                up = False
        if up:
            result.append("1")
        return ''.join(result[::-1])

    def addBinary(self, a: str, b: str) -> str:
        max_len = len(a) if len(a) >= len(b) else len(b)
        a = a.rjust(max_len, "0")[::-1]
        b = b.rjust(max_len, "0")[::-1]

        carry = False
        result = []
        for x, y in zip(a, b):
            # 두개가 다를때
            if x != y:
                result.append("0" if carry else "1")
            # 두개가 같을때
            else:
                result.append("1" if carry else "0")
                # x == y == 1 이라면 carry = 1, else 0
                carry = (x == "1")
        if carry:
            result.append("1")

        return ''.join(result[::-1])


s = Solution()
print(s.addBinary("11", "1"))
print(s.addBinary("1010", "1011"))
