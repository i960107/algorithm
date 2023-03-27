from sys import stdin

read = stdin.readline
N, Q = map(int, input().split())
numbers = list(map(int, read().split()))
numbers.sort()
prefix_sum = [0]
for x in numbers:
    prefix_sum.append(x + prefix_sum[-1])

for _ in range(Q):
    l, r = map(int, read().split())
    print(prefix_sum[r] - prefix_sum[l - 1])
