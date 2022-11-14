def solution(n: str) -> int:
    sum_odd = 0
    multi_even = 1

    def is_order_odd(index: int) -> bool:
        return (index + 1) % 2 == 1

    for index in range(7):
        if is_order_odd(index):
            sum_odd += int(n[index])
        else:
            multi_even *= (int(n[index]) if n[index] != "0" else 1)

    return (sum_odd * multi_even) % 10


for _ in range(5):
    print(solution(input()))
