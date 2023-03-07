from sys import stdin

read = stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

distances = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    distances[i][i] = 0

# 시작과 도착 도시를 연결하는 노선은 하나가 아닐 수 있다-> 최소로 선택
for _ in range(M):
    a, b, c = map(int, input().split())
    distances[a][b] = min(distances[a][b], c)

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            distances[a][b] = min(distances[a][b], distances[a][k] + distances[k][b])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(distances[i][j] if distances[i][j] != INF else 0, end=' ')
    print()
