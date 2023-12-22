from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        total = nums[right]
        while right < n - 1 and total < target:
            right += 1
            total += nums[right]

        if total < target:
            return 0

        min_len = right - left + 1

        # while문 for문?
        while left < n - 1:
            total -= nums[left]
            left += 1
            if right < n - 1:
                right += 1
                total += nums[right]
            # 무조건 window size 1이상이기 때문에 right 인덱스 체크해줄 필요는 없음.
            while total - nums[right] >= target:
                total -= nums[right]
                right -= 1
            if total >= target and right - left + 1 < min_len:
                min_len = right - left + 1
        return min_len

    def minSubArrayLenOptimized(self, target: int, nums: List[int]) -> int:
        # 원리는 똑같음. 일단 한번 찾은 윈도우 사이즈는 고려하지 않는다. 더 작은 사이즈만 찾는다.
        # 첫번째 윈도우 사이즈 찾는 것 따로 하지 않아도 됨.
        # r포인터 고정 -> l포인터 움직임.
        minLen = float("INF")

        l, sum = 0, 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minLen = min(minLen, r - l + 1)
                sum -= nums[l]
                l += 1
        return minLen if minLen <= len(nums) else 0


s = Solution()
print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1]))
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(4, [1, 4, 4]))
print(s.minSubArrayLen(4, [2, 2, 3, 4]))
