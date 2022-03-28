def solution_get_prime_num_count(n: int, k: int) -> int:
    answer = 0

    def make_notation(num: int, notation: int) -> str:
        reverse = ''
        while True:
            num, remainder = num // notation, num % notation
            reverse += str(remainder)
            if num == 0:
                break

        return reverse[::-1]

    # 00일경우 split 한결과 '' 포함됨 왜?
    # int('') = Exception
    primes = map(lambda x: int(x) if x else 0, make_notation(n, k).split('0'))

    def is_prime_number(num: int) -> bool:
        if num <= 1:
            return False
        # 제곱근까지 검사해야되는것 주의!!
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                return False
        else:
            return True

    return sum(1 for num in primes if is_prime_number(int(num)))


print(solution_get_prime_num_count(437674, 3))
print(solution_get_prime_num_count(1100011, 10))
