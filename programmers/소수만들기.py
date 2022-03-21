from itertools import combinations


def solution_prime_numbers(nums: list) -> list:
    # 전체 조합을 다 살펴봐야 하나? 최대 50C3->너무큰데?
    # 100000개 정도면 선형 탐색 가능?
    # 조합의 time complexity는? O(N)
    cnt = []
    for x, y, z in combinations(nums, 3):
        # O(n^2)  조합마다 소수인지 판별하기 위해서는 제곱근까지 살펴봐야함.
        num = x + y + z
        # 제곱근까지 살펴봐야. 제곱근이 정수이면 소수 아
        for denominator in range(2, int(num ** 0.5)+1):
            if num % denominator == 0:
                break
        else:
            cnt.append([x,y,z])
    return cnt


print(solution_prime_numbers([1, 2, 3, 4]))
print(solution_prime_numbers([1, 2, 7, 6, 4]))
