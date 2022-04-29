from typing import List
from collections import Counter


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    '''두 배열간 중복된 원소 출력'''
    # nusm2가 disk에 저장되어있고 크기가 커서 한번에 메모리에 로드하지 못한다면?
    nums1.sort()
    nums2.sort()
    c = Counter(nums1)
    answer = []
    for num in nums2:
        if c[num] > 0:
            # print(c.pop(num)) num의 개수 즉 value 나옴
            c[num] -= 1
            answer.append(num)
    return answer


def intersect_of_sorted_array(nums1: List[int], nums2: List[int]) -> List[int]:
    # 각 배열이 정렬된 상태라면 two pointer사용가능
    i = j = 0
    answer = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            answer.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return answer


# nums2가 num1에 비해 훨씬 더 길다면
# 한쪽의 배열의 크기가 무조건 작을 경우 어떻게 최적화 하는지
# 길이가 작은 배열을 순환하면서 각 원소의 값을 nums2에서 찾기. 긴 배열일수룍 LogN으로 탐색 시간 단축 큼

print(intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))

print(intersect_of_sorted_array(nums1=[1, 1, 2, 2], nums2=[2, 2]))
print(intersect_of_sorted_array(nums1=[4, 5, 9], nums2=[4, 4, 8, 9, 9]))
