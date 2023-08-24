class Solution(object):
    def merge_fail(self, nums1, m, nums2, n):
        result = []
        p1 = p2 = 0
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1

        while p1 < m:
            result.append(nums1[p1])
            p1 += 1

        while p2 < n:
            result.append(nums2[p2])
            p2 += 1

        nums1 = result

    def merge(self, nums1, m, nums2, n):
        result = []
        p1 = p2 = 0
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1

        while p1 < m:
            result.append(nums1[p1])
            p1 += 1

        while p2 < n:
            result.append(nums2[p2])
            p2 += 1

        for i in range(n + m):
            nums1[i] = result[i]

    def merge2(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1



arr = [3, 1, 2, 5, 4]
n = len(arr)
buff = [None] * n
s = Solution()
s.merge_sort(arr, 0, n - 1)
