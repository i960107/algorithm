import sys

# python은 재귀 호출 횟수가 1000회로 제한되어 있어
# 그 이상으로 쓰려면 제한을 늘려야함.
# 최대 1000개의 노드에서 나올 수 있는 간선의 수 1000*999 = 약 10^6
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[False] * (N + 1) for _ in range(N + 1)]  # 1-based 크기로 할당.0행 혹은 0열은 dummy
for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = True
    adj[b][a] = True

ans = 0
# 방문한 노드인지 체크
chk = [False] * (N + 1)
def dfs(i):
    for j in range(i,N+1):
        if adj[i][j] and not chk[j]:
            chk[j] = True
            dfs(j)

for i in range(1,N+1):
    ans += 1
    chk[i] = True
    dfs(i)

print(ans)

