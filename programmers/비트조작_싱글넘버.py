from typing import List


def single_numbers(nums: List[int]) -> int:
    '''XOR연산(Exclusive OR 배타적 연산)'''
    # 10진수의  XOR 연산:  4 ^ 0 = 4 다르면 그 숫자, 같으면 0
    # 2개씩 있는 요소들은 서로 상쇄되어 자라지고, 딱 하남나 있는 요소를 찾을 수 있다
    result = 0
    for num in nums:
        result ^= num
        print("result", result)
    return result


print(single_numbers([2, 2, 1]))
print(single_numbers([4, 1, 2, 1, 2]))
#  A ^ B ^ A = A ^ A ^ B = 0 ^ B = B
print(4 ^ 2 ^ 4)
