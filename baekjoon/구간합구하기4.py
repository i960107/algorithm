from sys import stdin

read = stdin.readline
N, M = map(int, input().split())
prefix_sum = [0]

for n in map(int, read().split()):
    if not prefix_sum:
        prefix_sum.append(n)
    else:
        prefix_sum.append(n + prefix_sum[-1])

# 맨 첫 인덱스 주의!
for _ in range(M):
    i, j = map(int, read().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
