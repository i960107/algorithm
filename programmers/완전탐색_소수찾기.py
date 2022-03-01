from math import sqrt
from itertools import permutations


def check(n: int):
    '''소수 판별하기'''
    # 소수 - 1과 자기자신으로만 나누어지는 2 이상의 자연수
    if n < 2:
        return False

    # 왜 n까지 검사하지않고 n의 제곱근까지만 검사하지?
    # 약수는 제곱근을 기준으로 대칭성을 가짐. 즉, 양의 제곱을 기준으로 앞뒤 쌍을 가짐.
    # O(sqrt(N))
    k = sqrt(n)

    for i in range(2, int(k) + 1):
        # 양의 제곱은 이하의 수들로 n을 나눠서 한번이라도 나누어 떨어지면 합성수
        if n % i == 0:
            return False
    else:
        return True


def solution(numbers: str) -> int:
    answer = []

    for k in range(1, len(numbers) + 1):
        per_list = list(map(''.join, permutations(list(numbers), k)))
        print(f'per_list : {per_list}')
        # set으로 캐스팅해서 중복 없애주기
        for num in set(per_list):
            if check(int(num)):
                answer.append(int(num))

    print(f'answer : {answer}')
    return len(set(answer))


print(a[:-1])
print(solution('17'))
print(solution('011'))

#에라토스테네스의 체?