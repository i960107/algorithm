from typing import List


class Solution:
    # prefix를 쓰나, sliding window를 쓰나 같은 원리임
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        window_sum = 0
        # 포인터를 어떻게 설정하느냐
        # 1. start = end가 될 수 있다. start, end 포함 winsum = nums[0]에서 시작. 옮기고 더한다.
        # 2. start포함, end 불포함. start =end = 0에서 시작, 더하고 포인터 이동
        # => end 포인터를 왼쪽이로 이동해줄때 end - 1값을 빼주저야함.
        # end는 포함하지 않는다
        while end < len(nums) and window_sum < target:
            window_sum += nums[end]
            end += 1

        if window_sum < target:
            return 0
        min_len = end - start

        while start < len(nums) - 1:
            window_sum -= nums[start]
            start += 1
            # end는 포함하지 않고 start는 포함하기 때문에 범위가 다름.
            if end < len(nums):
                window_sum += nums[end]
                end += 1

            while window_sum - nums[end - 1] >= target:
                window_sum -= nums[end - 1]
                end -= 1
            if window_sum >= target and end - start < min_len:
                min_len = end - start
        return min_len

    # 포인터가 같은 걸 가리킬 때 애매함.
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        start = end = 0
        window_sum = nums[0]

        while end < len(nums) - 1 and window_sum < target:
            end += 1
            window_sum += nums[end]

        if window_sum < target:
            return 0

        min_len = float('INF')
        while start < len(nums):
            window_sum -= nums[start]
            start += 1

            end += 1
            window_sum += nums[start]

            while window_sum - nums[end] >= target:
                window_sum -= nums[end]
                end -= 1

            if end - start + 1 < min_len:
                min_len = end - start + 1

    # 오른쪽 포인터를 고정
    # l, r포함.
    # 오또케 이러케 간단하지.
    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
        minlen = float('INF')
        l, sum = 0, 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minlen = min(r - l + 1, minlen)
                sum -= nums[l]
                l += 1
        return minlen if minlen <= len(nums) else 0


s = Solution()
print(s.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
print(s.minSubArrayLen(target=4, nums=[1, 4, 4]))
print(s.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(target=1, nums=[0, 1]))
print(s.minSubArrayLen(target=4, nums=[4]))
print(s.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 2]))

print(s.minSubArrayLen2(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
print(s.minSubArrayLen2(target=4, nums=[1, 4, 4]))
print(s.minSubArrayLen2(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen2(target=1, nums=[0, 1]))
print(s.minSubArrayLen2(target=4, nums=[4]))
print(s.minSubArrayLen2(target=7, nums=[2, 3, 1, 2, 4, 2]))
