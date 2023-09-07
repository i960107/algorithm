from typing import List


class Solution:
    # 오름차순 정렬되어있으면서 회전되어있다.
    # 1번에서 n번 rotete -> n번 rotate시 제자리로.
    # 중복된 원소는 없다.
    # O(LogN). 만약 O(N)이라면 선형탐색으로 값이 이전 값보다 작아지는 인덱스를 찾으면됨
    # 배열의 길이가 최소 1이다.
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[-1]:
                hi = mid - 1
            else:
                lo = mid + 1


s = Solution()
# print(s.findMin([3, 4, 5, 1, 2]))
# print(s.findMin([1, 2, 3, 4, 5]))
print(s.findMin([1]))
print(s.findMin([2, 3, 0]))
