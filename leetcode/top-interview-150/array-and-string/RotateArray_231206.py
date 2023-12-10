from typing import List


def rotate(nums: List[int], k):
    n = len(nums)
    # k가 n 이상일 수 있음!
    k %= n

    # 이렇게 하면 안됨 sort 포함. 배열을 뒤집어야함.
    # nums.sort(reverse=True)
    for i in range(n // 2):
        nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]

    for i in range(k // 2):
        nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]

    for i in range(0, (n - k) // 2):
        nums[k + i], nums[n - 1 - i] = nums[n - 1 - i], nums[k + i]


def rotate2(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n

    i, j = 0, n - 1

    # 배열을 뒤집을때는 for문보다 while문이 편리
    # 첫번째, 끝 원소가 지정해주고 i < j를 종료조건으로 하면 몇개를 뒤집어야할지 복잡한 계산이 필요없음.
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    i, j = 0, n - k - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    i, j = n - k, n - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    print(nums)


# 홀수개일때
rotate2([1, 2, 3, 4, 5], 3)
# 짝수개일때
rotate2([1, 2, 3, 4], 2)
rotate2([-1, -100, 3, 99], 2)
