from collections import Counter
from math import floor, ceil
from typing import List


def solution_avg(l: list) -> int:
    return sum(l) / len(l)


# print(solution_avg([1, 2, 3, 4]))
# print(solution_avg([5, 5]))

def solution_sort(string: list, n: int) -> list:
    return sorted(string, key=lambda x: (x[n], x))


print(solution_sort(["sun", "bed", "car"], 1))
print(solution_sort(["abce", "abcd", "cdx"], 2))


def solution_failure(N: int, stages: list) -> list:
    s = [i + 1 for i in range(N)]
    failures = [0] * N

    counter = Counter(stages)
    # dicionary 항상 가져올때 None 주의!!
    reached = counter.get(N + 1, 0)

    for stage in range(N, 0, -1):
        reached += counter.get(stage, 0)
        if reached:
            failure = counter.get(stage, 0) / reached
        else:
            failure = 0
        failures[stage - 1] = failure

    # zip은 tuple로 반환?
    return [s for _, s in sorted(zip(failures, s), key=lambda x: (x[0], -x[1]), reverse=True)]


print(solution_failure(5, [2, 1, 2, 6, 4, 3, 3]))
print(solution_failure(4, [4, 4, 4, 4, 4]))


def solution_pokemon(nums: list) -> int:
    kind = 0
    counter = Counter(nums)
    if len(counter) >= (len(nums) // 2):
        kind = len(nums) // 2
    else:
        kind = len(counter)
    return kind


print(solution_pokemon([3, 1, 2, 3]))
print(solution_pokemon([3, 3, 3, 2, 2, 4]))
print(solution_pokemon([3, 3, 3, 2, 2, 2]))


def solution_matrix(arr1: list, arr2: list) -> list:
    '''행렬의 덧셈'''
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]


def solution_medium(s: str) -> str:
    start = floor((len(s) - 1) / 2)
    end = ceil((len(s) - 1) / 2)
    return s[start:end + 1]
    # return str[(len(str)-1)//2:(len(str)//2)+1]


print(solution_medium('abcde'))
print(solution_medium('qwer'))


def solution_2016(a: int, b: int) -> str:
    days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day_of_week = ['MON', 'TUE', "WED", "TUR", "FRI", "SAT", "SUN"]
    month, day = 1, 1

    # a월 b일 직후 금요일 찾기
    while (month < a) or (month == a and day < b):
        if day + 7 <= days[month]:
            day += 7
        else:
            day = 7 - (days[month] - day)
            month += 1

    # 금요일 인덱스
    friday = 4
    if month != a:
        return day_of_week[friday - (days[a] - b + day)]
    else:
        return day_of_week[friday - (day - b)]


def solution_2016_others(a: int, b: int) -> str:
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ['FRI', 'SAT', 'SUN', "MON", 'TUE', "WED", 'THU']
    # 두 날의 날짜 차이를 계산한후 인덱스 돌려서 요일 계산
    return day_of_week[(sum(months[:a - 1]) + b - 1) % 7]


print(solution_2016_others(5, 24))
print(solution_2016_others(4, 29))
print(solution_2016_others(4, 26))
print(solution_2016_others(12, 30))
print(solution_2016_others(12, 31))
print(solution_2016_others(1, 1))
print(solution_2016_others(5, 31))


def solution_ternary_reverse(n: int) -> int:
    # int() : n진수 -> 10진수로 바꾸는 함수
    # 10진수 -> n진수 변환은 직접 구현 필요

    reversed_ternary = ''
    share, remainder = n, 0
    while True:
        share, remainder = share // 3, share % 3
        reversed_ternary += str(remainder)
        if share == 0:
            break
    return int(reversed_ternary, 3)


print(solution_ternary_reverse(45))
print(solution_ternary_reverse(125))


def solution_find_minimum_divisor(n: int) -> int:
    '''나머지가 1이 되는 수 찾기'''
    for i in range(2, n):
        if (n - 1) % i == 0:
            return i


print(solution_find_minimum_divisor(10))
print(solution_find_minimum_divisor(12))
print(solution_find_minimum_divisor(1000000))


def solution_secret_map(n: int, arr1: List[int], arr2: List[int]) -> int:
    def to_binary(num: int) -> List[int]:
        binary = [0] * n
        for i in range(-1, -n - 1, -1):
            binary[i] = num % 2
            num = num // 2
        return binary

    for i in range(n):
        arr1[i] = to_binary(arr1[i])
        arr2[i] = to_binary(arr2[i])

    answer = []
    for a1, a2 in zip(arr1, arr2):
        curr = ''
        for i in range(n):
            if a1[i] + a2[i] == 0:
                curr += " "
            else:
                curr += "#"
        answer.append(curr)
    return answer


print(solution_secret_map(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution_secret_map(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))


def solution_sum_divisor(n: int) -> int:
    l = []
    answer = 0
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            num1, num2 = x, n // x
            l.append(num1)
            l.append(num2)
            answer += num1
            if num1 != num2:
                answer += num2
    print(l)
    return answer


print(solution_sum_divisor(1))
print(solution_sum_divisor(16))
print(solution_sum_divisor(12))
print(solution_sum_divisor(5))


def solution_ceasar_encryption(s: str, n: int) -> str:
    answer = ''
    for c in s:
        if c.islower():
            moved = (ord(c) + (n % 26))
            encrypted = chr(moved) if moved <= ord('z') else chr(moved - 26)
            answer += encrypted
            # chr((ord(c) - ord('a') + n) % 26) + ord('a')
        elif c.isupper():
            moved = (ord(c) + (n % 26))
            encrypted = chr(moved) if moved <= ord('Z') else chr(moved - 26)
            answer += encrypted
        else:
            answer += c
    return answer


print(solution_ceasar_encryption("AB", 1))
print(solution_ceasar_encryption("z", 1))
print(solution_ceasar_encryption("a B z", 4))

print('Zbcdefg')


def solution_odd_character(s: str) -> str:
    answer = ''

    # 전체 인덱스
    p1 = 0
    # 그룹 내 인덱스
    p2 = 0
    while p1 < len(s):
        # '' : Falsy ' 'Truthy
        if s[p1] == ' ':
            answer += s[p1]
            p2 = 0
        else:
            answer += s[p1].upper() if p2 % 2 == 0 else s[p1].lower()
            p2 += 1
        p1 += 1

    return answer


# print(solution_odd_character("try hello world"))
# print(solution_odd_character(""))
# print(solution_odd_character("try"))
print(solution_odd_character("  world"))


def solution_prime_numbers(n: int) -> int:
    '''소수찾기'''
    answer = 0

    def isPrimeNumber(num: int) -> bool:
        for x in range(2, int(num ** 0.5) + 1):
            if num % x == 0:
                return False
        return True

    for num in range(2, n + 1):
        if isPrimeNumber(num):
            answer += 1

    return answer


def solution_prime_numbers_others(n: int) -> int:
    '''소수찾기: 에라토스테너스의 체'''
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            # i 자체는 소수.
            num -= set(range(2 * i, n + 1, i))
    return len(num)


print(solution_prime_numbers(10))
print(solution_prime_numbers(5))
