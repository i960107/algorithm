class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result = []
        p1 = p2 = 0
        temp = nums[1].deepcopy()
        while p1 < m or p2 < n:
            if p1 < m and p2 < n:
                if temp[p1] < nums2[p2]:
                    p1 += 1
                else:
                    result.append(nums2[p2])
                    p2 += 1
            elif p1 == m:
                result.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                result.append(nums1[p1])
                p1 += 1
        nums1 = result
        print(nums1)

                

