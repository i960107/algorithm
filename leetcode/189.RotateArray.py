from typing import List
from collections import deque


def rotate_fail(nums: List[int], k: int) -> None:
    # Do not return anything modify nums in-place instead
    # O(1) : takes the same amount of space regardless of the input size
    count = 0
    index = 0
    temp = nums[0]

    # 실패 이유. 같은 자리 여러번 바뀔 수 있음. rotate된 자리가 상호적일때
    while count < len(nums):
        count += 1
        rotated_index = (index + k) % len(nums)
        temp, nums[rotated_index] = nums[rotated_index], temp
        index = rotated_index

    print(nums)


def rotate(nums: List[int], k: int) -> None:
    # i,j = start, end indices inclusive
    def reverse(arr, i, j):
        i_t = 0
        while i_t <= (j - i) // 2:
            arr[i + i_t], arr[j - i_t] = arr[j - i_t], arr[i + i_t]
            i_t += 1

    n = len(nums)

    # 우리의 목표! i -> (i+k) % len(nums) 로 옮기기
    # reverse the whole array
    # i -> n-1-i
    reverse(nums, 0, n - 1)

    # reverse first subarray
    # k-1-(n-1-i) = k-n +i
    # i+k-n>=0 따라서 k -n +k = (i+k)  %n
    reverse(nums, 0, k - 1)

    # reverse second subarray
    # k + (n-k-1) -(n-1-i-k) = i +k
    reverse(nums, k, n - 1)

    print(nums)


print(rotate(nums=[-1, -100, 3, 99], k=2))
print(rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
