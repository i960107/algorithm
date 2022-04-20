from typing import List, Tuple


def move_zeros_fail(nums: [List[int]]) -> None:
    def sort_by(enum: Tuple[int, int]) -> int:
        if enum[1] == 0:
            return len(nums)
        else:
            return enum[0]

    # sort에서 index사용하기?실패
    enumerate(nums).sort(key=sort_by)
    print(nums)


def move_zeros_optimal(nums: [List[int]]) -> None:
    '''선형 배열 조작하기'''
    # all elements before the slow pointer are non-zeros
    # all elemetns between curr and slow pointer are zeros

    # both requirement(0 to end, others maintain their relative position) are mutually exclusive
    # you can solve the individual sub-problems then combine
    last_none_zero = 0
    for curr in range(len(nums)):
        # 0을 모두 앞으로 보내고 싶다면!
        # if nums[curr] == 0:
        # 어떻게 last non zero 앞은 다 non zero가 되지? 
        if nums[curr] != 0:
            # fill the current position by 0 right away,so we don't need to come back
            nums[last_none_zero], nums[curr] = nums[curr], nums[last_none_zero]
            # 왜 1만 증가해줘도 될까?
            last_none_zero += 1
            print(nums)
    print(nums)


def move_zeros1(nums: [List[int]]) -> None:
    '''space sub-optimal'''
    # space complexity O(N). Time Complexity O(N)
    # 인터뷰였다면 이렇게 풀 수 있지만 이 경우 복잡도가 sub optimal 라는 설명으로 시작한다면 굳!
    # 다음으로 optimal 전략 소
    n = len(nums)

    # 1단계. count the zeros
    zeros = 0
    for num in nums:
        zeros += 1 if num == 0 else 0

    # 2단계. make all the non-zero elements retain their original order
    result = []
    for num in nums:
        if num != 0:
            result.append(num)

    # 3단계 move all zeros  to the end
    result += [0] * zeros

    # 4단계 combin the result
    nums = result
    print(nums)


def move_zeros2(nums: [List[int]]) -> None:
    '''two pointer approach'''
    # time complexity O(N) space complexity O(1)
    last_non_zero = 0
    for curr in range(len(nums)):
        # append non-zero-element just in front of the last non 0 element we found
        if nums[curr] != 0:
            # 앞에서부터 채워나간다는 느낌
            nums[last_non_zero] = nums[curr]
            last_non_zero += 1
        # all the non-zero elements are already at the beginning
        # we just need to fill remaining array with 0's

    for i in range(last_non_zero, len(nums)):
        nums[i] = 0
    print(nums)


print(move_zeros_optimal(nums=[0, 1, 0, 3, 12]))
print(move_zeros_optimal(nums=[0]))
