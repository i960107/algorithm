from math import trunc


def tax_simulation(money: int, min_ratio: int, max_ratio: int, rank_size: int, threshold: int, months: int) -> int:
    def get_tax_ratio(amount_of_ownership: int) -> float:
        if amount_of_ownership < threshold:
            return 0
        return min(min_ratio + ((amount_of_ownership - threshold) // rank_size), max_ratio)

    for month in range(months):
        amount_of_ownership = trunc(money * 0.01) * 100
        tax_ratio = get_tax_ratio(amount_of_ownership)
        money -= (amount_of_ownership * tax_ratio / 100)

    return int(money)


print(tax_simulation(12345678, 10, 20, 250000, 10000000, 4))
print(tax_simulation(1000000000, 50, 99, 100000, 0, 6))
print(tax_simulation(123456789, 0, 0, 1, 0, 360))
