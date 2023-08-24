from collections import deque


# edge case : k가 nums배열의 길이보다 클 수 있다.


class Solution(object):

    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        temp = nums[n - k:] + nums[:n - k]
        for i in range(len(nums)):
            nums[i] = temp[i]

    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        temp = [None] * n
        for i in range(n):
            temp[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = temp[i]

    def rotate(self, nums, k):
        d = deque(nums)
        k = k % len(nums)
        for _ in range(k):
            popped = d.pop()
            d.appendleft(popped)
        for i in range(len(nums)):
            nums[i] = d[i]
