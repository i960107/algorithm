from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        up = False
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += up
            up, digits[i] = divmod(digits[i], 10)
            if not up:
                break
        return digits if not up else [1] + digits


s = Solution()
print(s.plusOne([9]))
print(s.plusOne([1, 2, 3, 9]))
