from typing import List


def maxDistance(nums1: List[int], nums2: List[int]) -> int:
    out = 0
    for i in range(len(nums1)):
        left = i
        right = len(nums2) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums1[i] <= nums2[mid]:
                left = mid + 1
                if (mid - i) > out:
                    out = mid - i
            else:
                right = mid - 1
    return out


print(maxDistance(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]))
print(maxDistance(nums1=[2, 2, 2], nums2=[10, 10, 1]))
print(maxDistance(nums1=[30, 29, 19, 5], nums2=[25, 25, 25, 25, 25]))
print(maxDistance(nums1=[2, 2, 2], nums2=[10, 10, 1]))
