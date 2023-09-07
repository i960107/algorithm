from typing import List


class Solution:
    # 정렬된 배열.
    # 중복된 원소 없음.
    # 왼쪽으로 rotate된 배열.
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        k = 0
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid - 1]:
                k = mid
                break
            if nums[mid] < nums[-1]:
                hi = mid - 1
            else:
                lo = mid + 1

        # 주의해야함 왼쪽으로 돌릴때 오른쪽으로 돌릴
        k = len(nums) - k

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            rotated_mid = (mid - k) % len(nums)
            value = nums[rotated_mid]
            if value == target:
                return rotated_mid
            elif value < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return - 1


s = Solution()

# print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
# print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
# print(s.search([1], 3))
print(s.search([3, 5, 1], 5))
print(s.search([1, 3, 5], 5))
