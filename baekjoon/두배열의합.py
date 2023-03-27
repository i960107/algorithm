from sys import stdin
from collections import defaultdict

read = stdin.readline

T = int(read())

N = int(read())

arr_n = list(map(int, read().split()))

prefix_n = [0]
for x in arr_n:
    prefix_n.append(prefix_n[-1] + x)

M = int(read())

arr_m = list(map(int, read().split()))

prefix_m = [0]
for x in arr_m:
    prefix_m.append(prefix_m[-1] + x)

count = 0
cases = defaultdict(int)
# O(N^2)
# 헐 음수도 됨...
for j in range(1, N + 1):
    for i in range(j, N + 1):
        cases[prefix_n[i] - prefix_n[j - 1]] += 1

for j in range(1, M + 1):
    for i in range(j, M + 1):
        me = prefix_m[i] - prefix_m[j - 1]
        counterpart = cases[T - me]
        count += counterpart

print(count)