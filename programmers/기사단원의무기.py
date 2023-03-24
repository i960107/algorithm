def solution(number: int, limit: int, power: int) -> int:
    def get_divisor_count(num: int) -> int:
        divisors = 0
        for n in range(1, int(num ** 0.5) + 1):
            if num % n != 0:
                continue
            if n * n!= num:
                divisors += 2
            else:
                divisors += 1
        return divisors

    total_steel = 0
    for person in range(1, number + 1):
        weapon = get_divisor_count(person)
        if weapon > limit:
            weapon = power
        total_steel += weapon
    return total_steel


print(solution(10, 3, 2))
print(solution(5, 3, 2))
