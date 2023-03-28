from typing import List


# 상관없이 교점 식 유도 가능. 최소 공배수 아니어도 공배수만 만들어서 x혹은 y제거해줄 수 있으면 됨
def get_lcm(a: int, b: int) -> int:
    gcd = get_gcd(a, b)
    return a // gcd * b // gcd * gcd


def get_gcd(a: int, b: int) -> int:
    # a가 더 큰 수가 되도록
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def solution(line: List[List[int]]) -> List[str]:
    cross = set()
    # min_x, min_y = 1001, 1001
    # # x좌표 주의!
    # max_x, max_y = -1001, -1001
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            if a * d - b * c == 0:
                continue
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            if x != int(x) or y != int(y):
                continue
            x = int(x)
            y = int(y)
            cross.add((x, y))
            # 가장 첫값은 minx 이면서 maxx인데 제대로 초기화 안됨.
            # if x < min_x:
            #     min_x = x
            # elif x > max_x:
            #     max_x = x
            # if y < min_y:
            #     min_y = y
            # elif y > max_y:
            #     max_y = y
    # 한번씩 비교해주는 것 보다 min으로 한번에 비교하면 통과됨.?
    # N ^ 2 * 4번의 연산
    # N ^ 2 // 2 *4 번의 연산...
    min_x = min([x for x, y in cross])
    max_x = max([x for x, y in cross])
    min_y = min([y for x, y in cross])
    max_y = max([y for x, y in cross])

    board = [["."] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for x, y in cross:
        # 좌표를 4사분면으로 옮긴다고 생각
        r, c = max_y - y, x - min_x
        board[r][c] = "*"

    answer = []
    for row in board:
        answer.append(''.join(row))

    return answer


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
