from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        up = True

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += (up)
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                up = True
            else:
                up = False
                break
        return digits if not up else [1] + digits


s = Solution()
print(s.plusOne([1, 9, 9, 9]))
print(s.plusOne([9, 9, 9]))
print(s.plusOne([1, 2, 3, 4]))
