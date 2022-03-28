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
    answer = 0
    n = 1
    while True:
        curr = arr[-1] * n

        n += 1
    return answer


# print(solution_common_multiple([2, 6, 8, 14]))
# print(solution_common_multiple([1, 2, 3]))


def solution_candidate_key(relation: list) -> int:
    unique = 0
    non_unique = {}

    for i in range(len(relation[0])):
        counter = Counter(relation[j][i] for j in range(len(relation)))
        # 중복된 원소가 있을때
        if len(counter) != len(relation):
            # 고유키가 아닌 키들과 복합키가 기본키가 될 수 있는지 살피기
            non_unique[i] = [key for key in counter if counter[key] > 1]
        # 중복된 원소가 없을때
        else:
            unique += 1

    # 중복된 컬럼들끼리 복합키가 후보키 될 수 있을지 검사
    # non_unique 배열은 오름차순 정렬된 상태. 자기 보다 뒤 키만 확인하면 됨.
    # 확인하고 기본키 가능하면 두개 배열에서 제거하기
    # 중복값 검사!!
    # 세개 합쳐서 복합키 될 수도 있음. 어떻게 검사하지?
    for i in non_unique:
        for j in non_unique:
            counter = Counter(relation[k][i] + relation[k][j] for k in range(len(relation))
                              if relation[k][i] in non_unique[i])
            if all(v <= 1 for v in counter.values()):
                unique += 1
    return unique


print(solution_candidate_key(
    [["100", "ryan", "music", "2"],
     ["200", "apeach", "math", "2"],
     ["300", "tube", "computer", "3"],
     ["400", "con", "computer", "4"],
     ["500", "muzi", "music", "3"],
     ["600", "apeach", "music", "2"]]))


def solution_fibo_iterative(n: int) -> int:
    fibo = 0
    f0 = 0
    f1 = 1
    curr = 1

    while curr < n:
        fibo = f0 + f1
        curr += 1
        f0, f1 = f1, fibo
    return fibo % 1234567


def solution_fibo_others(n: int) -> int:
    # a : before, b:curr
    a, b = 0, 1

    for i in range(n):
        # n ==2 이면 두번 수행
        # 첫번째 수행 a, b = 1,1
        # 두번째 수행 a, b = 1,2
        a, b = b, a + b
    return a % 1234567


def solution_fibo_recursive(n: int) -> int:
    fibo = 0
    f1 = 0
    f2 = 1
    return fibo % 1234567


print(solution_fibo_iterative(3))
print(solution_fibo_iterative(5))
print(solution_fibo_recursive(3))
print(solution_fibo_recursive(5))
