from typing import List
from collections import Counter


def solution_124_country(n: int) -> int:
    '''124나라의 숫자'''
    numbers = ['1', '2', '4']
    answer = ''
    group, order = (n - 1) // 3, (n - 1) % 3
    answer += numbers[order]
    return answer


print(solution_124_country(1))
print(solution_124_country(2))
print(solution_124_country(3))
print(solution_124_country(4))


def solution_tuple(s: str) -> List[int]:
    # 가장 빈번히 나온 문자가 튜플의 맨 앞 원소가 됨
    elements = [y for x in s[2:-2].split('},{') for y in x.split(',')]
    # elements = s.lstrip('{').rstrip('}').split('},{')
    counter = Counter(elements)
    # list comprehensing 다중 for문!!
    answer = [int(x[0]) for x in counter.most_common()]

    return answer


print(solution_tuple("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution_tuple("{{2},{2,1},{1,2,3},{2,1,3,4}}"))
print(solution_tuple("{{20,111},{111}}"))
print(solution_tuple("{{123}}"))
print(solution_tuple("{{4,2,3},{3},{2,3,4,1},{2,3}}"))


def solution_rectangle(W: int, H: int) -> int:
    '''멀쩡한 사각형'''

    # 왜 안될까
    # H가 1씩 늘어날때마다 옆으로 전진하는 거리
    advance = W / H

    n = 1
    # W/H가 처음으로 정수가 되는 때
    while int(advance * n) != (advance * n):
        n += 1

    # W/H 의 배수의 개수+ range(W)의 개수 - range(W)공통된 개수
    spoiled = W // advance + W - (W // (advance * n))
    return W * H - int(spoiled)


def solution_rectangle_others(W: int, H: int) -> int:
    # 크기 비교 안 해도 되나?
    def gcd(a: int, b: int):
        return b if a % b == 0 else gcd(b, a % b)

    # w와 h가 공약수가 있다면 문제를 공약수를 나눈 w'와 h'로 축소시킬 수 있음
    # ( w' + h' -1 ) gcd
    broken = W + H - gcd(W, H)
    return W * H - broken


print(f'멀쩡한 삼각형 수 {solution_rectangle(8, 12)}')
print(f'멀쩡한 삼각형 수 {solution_rectangle(3, 3)}')
print(f'멀쩡한 삼각형 수 {solution_rectangle(2, 4)}')
print(f'멀쩡한 삼각형 수 {solution_rectangle(3, 2)}')


def solution_GCD_LCM(n: int, m: int) -> List[int]:
    def get_gcd(a: int, b: int) -> int:
        # 서로 나누어 0이 될때까지 나머지 구하기
        mod = a % b
        if mod != 0:
            a, b = b, mod
            return get_gcd(a, b)
        else:
            return b

    if m >= n:
        gcd = get_gcd(m, n)
    else:
        gcd = get_gcd(m, n)
    return [gcd, int(m * n / gcd)]


print(solution_GCD_LCM(3, 12))
print(solution_GCD_LCM(2, 5))


def solution_common_multiple(arr: List[int]) -> int:
    '''N개 숫자의 최소공배수'''
    # 유클리드 호제법 : 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘.
    # a를 b로 나눈 나머지를 r이라고 하면(단, a>b) 최대 공약수는 b와 r의 최대공약수와 같다
    # 최소공배수 (A*B)/GCD
    # 정렬 후 가장 큰 값의 배수를 확인하기
    arr.sort()
    n = 1
    while True:
        curr = arr[-1] * n

        n += 1
    return answer


print(solution_common_multiple([2, 6, 8, 14]))
print(solution_common_multiple([1, 2, 3]))
