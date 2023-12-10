# 새로운 배열을 만드는 것이 아니라 nums1에서 정렬해야함.
def merge(nums1, m, nums2, n):
    p1 = p2 = 0
    index = 0
    while p1 < m and p2 < n:
        if nums1[p1] <= nums2[p2]:
            nums1[index] = nums1[p1]
            p1 += 1
        else:
            nums1[index] = nums2[p2]
            p2 += 1
        index += 1
    print(nums1)
    for i in range(p1, m):
        nums1[index] = nums1[i]
        index += 1
    for i in range(p2, n):
        nums1[index] = nums2[i]
        index += 1
    print(nums1)


merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
merge(nums1=[1], m=1, nums2=[], n=0)
