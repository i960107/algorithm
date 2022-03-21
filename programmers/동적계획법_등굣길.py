def solution(m: int, n: int, puddles: list) -> int:
    # 2차원 배열 만들때 주의!! 배열*숫자로 만들면 같은 주소 참조하게 배열됨.
    # 원소 배열은 [0] 즉, 기본형인 숫자를 원소로 하기 때문에 주소가 복사되지 않음
    path = [[0] * m for _ in range(n)]
    path[0][0] = 1
    # O(N) N:은 지역
    for x, y in puddles:
        path[y - 1][x - 1] = None
    for i in range(len(path)):  # n 세로 -> 세로로 탐색후 다음 열로 넘어가기 -> 괜찮음. 가로 탐색을 하려면
        # puddles를 미리 다 None으로 만들어야함. 안 그럼 탐색 순서에 따라 결과 달라짐
        # len(path) : n 세로 길이를 말함. len[j][j] 가 path에서 m,n을 나타냄
        for j in range(len(path[i])):  # i가 세로, j가 가로를 나타냄 path[i,j]
            if i + j == 0 or path[i][j] is None:
                continue
            # not path[i][j]로 검사 불가. 0도 Falsy
            cnt = 0
            cnt += path[i - 1][j] if i > 0 and path[i - 1][j] else 0
            cnt += path[i][j - 1] if j > 0 and path[i][j - 1] else 0
            path[i][j] = cnt

    return path[n - 1][m - 1] % 1000000007


print(solution(4, 3, [[2, 2], [3, 2]]))
