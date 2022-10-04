from itertools import combinations_with_replacement


def solution(num: int) -> int:
    tri_num = [n * (n + 1) / 2 for n in range(1, 46)]

    for t1, t2, t3 in combinations_with_replacement(tri_num, 3):

        if t1 + t2 + t3 == num:
            return 1

    return 0


res = solution(10)
print(res, res == 1)

res = solution(20)
print(res, res == 0)

res = solution(1000)
print(res, res == 1)
