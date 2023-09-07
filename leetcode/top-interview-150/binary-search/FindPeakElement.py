from typing import List


class Solution:
    # 이웃한 원소들보다 클때 peak이라고 함.
    # 여러개의 peak이 존재할 수 있고 아무거나 반환하면 됨.
    # 배열의 바깥은 음의 무한대로 간주, 즉, 배열의 원소들은 항상 배열 바깥의 원소들보다 크다고 간주
    # O(LogN)시간 알고리즘 선형 검사 할 수 없음
    # 이웃한 원소들과 값이 같을 수 없음. 원소는 음수가 될 수 있음
    # 정렬되어있지 않은 배열.
    # 길이는 최소1
    # 최고로 높은 봉우리를 찾으면 되는 건데 이진 검색은 불가능.
    def findPeakElement(self, nums: List[int]) -> int:
        def find_peak(left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            left_peak = find_peak(left, mid)
            right_peak = find_peak(mid + 1, right)
            # print("left%d right%d peak%d" % (left, right, max(nums[left_peak], nums[right_peak])))
            # print("left_peak%d right_peak%d " % (left_peak, right_peak))
            return left_peak if nums[left_peak] > nums[right_peak] else right_peak

        return find_peak(0, len(nums) - 1)


s = Solution()
print(s.findPeakElement([1, 2, 3, 1]))
print(s.findPeakElement([2]))
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(s.findPeakElement([1, 2, 3, 4, 5, 6]))
