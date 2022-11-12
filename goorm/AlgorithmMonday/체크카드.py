from sys import stdin
from typing import List, Tuple
from collections import deque


def get_account_balance_after_transactions(N: int, transactions: List[Tuple[str, int]]) -> int:
    reservations = deque()

    def deposit(money: int):
        nonlocal N
        N += money
        pay_reserve_if_possible()

    def pay(money: int):
        nonlocal N
        if N >= money:
            N -= money

    def reserve(money: int):
        reservations.append(money)
        pay_reserve_if_possible()

    def pay_reserve_if_possible():
        nonlocal N
        while reservations and reservations[0] <= N:
            N -= (reservations.popleft())

    for t, amount in transactions:

        if t == "deposit":
            deposit(amount)

        elif t == "reservation":
            reserve(amount)

        else:
            pay(amount)

    return N


read = stdin.readline
N, M = map(int, input().split())

transactions = []
for _ in range(M):
    t, amount = read().split()
    transactions.append((t, int(amount)))

print(get_account_balance_after_transactions(N, transactions))
