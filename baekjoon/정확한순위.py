N, M = map(int, input().split())
# 학생들간의 거리를 정할 순 없는데. 순서만 알 수 있지..
# 다익스트라 해서 모든 학생들과의 거리가 정해져있으면 -> INF가 아니면 알 수 있음
# True, False, None로 정해볼까?
is_higher = [[None] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    is_higher[i][i] = False

for _ in range(M):
    a, b = map(int, input().split())
    is_higher[a][b] = False
    is_higher[b][a] = True

# 도달이 가능하다면 성적 비교가 가능하다
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if is_higher[a][k] and is_higher[k][b]:
                is_higher[a][b] = True

count = 0
# 각 학생을 번호에 따라 한 명씩 확인하면 도달 가능한지 체크
# a -> b가 도달가능하다면 b -> a 도 도달가능하지 않나. 양방향 그래프이니깐
for row in is_higher:
    print(row)
    defined = True
    for index in range(1, N + 1):
        # if not row[index] :
        if row[index] is None:
            defined = False
            break
    if defined:
        count += 1

print(count)
