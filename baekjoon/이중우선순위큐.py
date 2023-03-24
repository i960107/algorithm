import sys, heapq
from collections import defaultdict


def push(n: int):
    count_dict[n] += 1
    heapq.heappush(min_h, n)
    heapq.heappush(max_h, -n)


def pop_min():
    while min_h:
        c = heapq.heappop(min_h)
        if count_dict[c] > 0:
            count_dict[c] -= 1
            break


def pop_max():
    while max_h:
        c = -heapq.heappop(max_h)
        if count_dict[c] > 0:
            count_dict[c] -= 1
            break


ipt = sys.stdin.readline
opt = sys.stdout.write

t = int(ipt())
for _ in range(t):
    k = int(ipt())
    max_h, min_h = [], []
    count_dict = defaultdict(int)
    for _ in range(k):
        op, n = ipt().split()
        n = int(n)
        if op == 'I':
            push(n)
        elif op == 'D':
            if n == 1:
                pop_max()
            else:
                pop_min()

    sorted_items = sorted(num for num, count in count_dict.items() if count > 0)
    if sorted_items:
        print(sorted_items[-1], sorted_items[0])
    else:
        opt('EMPTY\n')
