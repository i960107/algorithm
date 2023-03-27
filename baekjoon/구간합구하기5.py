from sys import stdin

read = stdin.readline
N, M = map(int, input().split())
arr = [[0] * (N + 1)]
for _ in range(N):
    arr.append([0] + list(map(int, read().split())))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        arr[i][j] += arr[i][j - 1]

for j in range(1, N + 1):
    for i in range(1, N + 1):
        arr[i][j] += arr[i - 1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, read().split())
    print(arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1])
