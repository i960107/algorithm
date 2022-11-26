from math import trunc


class TaxPolicy:
    def __init__(self, min_ratio: int, max_ratio: int, rank_size: int, threshold: int):
        self.min_ratio = min_ratio
        self.max_ratio = max_ratio
        self.rank_size = rank_size
        self.threshold = threshold

    def calculate_assumed_amount(self, money: int) -> int:
        return trunc(money * 0.01) * 100

    def calculate_tax_ratio(self, assumed_amount: int) -> int:
        if assumed_amount < self.threshold:
            return 0

        tax_ratio = min(self.max_ratio
                        , self.min_ratio + (assumed_amount - self.threshold) // self.rank_size)
        return tax_ratio

    def calculate_tax_(self, money: int) -> float:
        assumed_amount = self.calculate_assumed_amount(money)
        tax_ratio = self.calculate_tax_ratio(assumed_amount)
        return assumed_amount * tax_ratio / 100


def simulate_tax_policy(money: int, min_ratio: int, max_ratio: int, rank_size: int, threshold: int, months: int) -> int:
    tax_policy = TaxPolicy(min_ratio, max_ratio, rank_size, threshold)

    for _ in range(months):
        money -= tax_policy.calculate_tax_(money)

    return int(money)


print(simulate_tax_policy(12345678, 10, 20, 250000, 10000000, 4))
print(simulate_tax_policy(1000000000, 50, 99, 100000, 0, 6))
print(simulate_tax_policy(123456789, 0, 0, 1, 0, 360))
