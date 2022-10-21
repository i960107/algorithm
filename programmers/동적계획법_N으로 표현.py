def get_minimum_count_N_used(N: int, number: int) -> int:
    memo = [set() for _ in range(9)]

    for count in range(1, 9):
        numbers = memo[count]
        numbers.add(int(str(N) * count))

        for mid in range(1, count // 2 + 1):
            for x in memo[mid]:
                for y in memo[count - mid]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(y - x)
                    numbers.add(x * y)
                    if y:
                        numbers.add(x // y)
                    if x:
                        numbers.add(y // x)

        memo[count] = numbers

        if number in numbers:
            return count

    return -1


print(get_minimum_count_N_used(5, 12))
print(get_minimum_count_N_used(2, 11))
