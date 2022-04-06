from typing import List


def two_sum_of_sorted(nums: List[int], target: int) -> List[int]:
    # 정렬된 경우에만 사용가능!
    l, u = 0, len(nums) - 1
    num = nums[l] + nums[u]
    while num != target:
        if num < target:
            l += 1
        else:
            u -= 1
        num = nums[l] + nums[u]
    return [l, u]


def two_sum(nums: List[int], target: int) -> List[int]:
    # 정렬이 안된 배열에서 two sum 구하기 -> BruteForce밖에 안됨!
    # 정렬된 인덱스를 가져오기!
    indices = [i for i in range(len(nums))]
    indices.sort(key=lambda x: nums[x])

    print(f'indices {indices}')

    l, u = 0, len(nums) - 1

    num = nums[indices[l]] + nums[indices[u]]

    while num != target:
        if num < target:
            l += 1
        else:
            u -= 1
        num = nums[indices[l]] + nums[indices[u]]
    return [indices[l], indices[u]]


print(two_sum(nums=[-1, -2, -3, -4, -5], target=-8))  # [0,1]
print(two_sum(nums=[2, 7, 11, 15], target=9))  # [0,1]
print(two_sum(nums=[3, 2, 4], target=6))  # [1,2]
print(two_sum(nums=[3, 3], target=6))  # [0,1]
