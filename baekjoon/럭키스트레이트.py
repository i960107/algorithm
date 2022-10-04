def solution(n: int) -> str:
    str_n = str(n)

    tot = 0
    for i, c in enumerate(str_n):

        if i < len(str_n) // 2:

            tot += int(c)
        else:
            tot -= int(c)

    return "LUCKY" if not tot else "READY"


print(solution(123402))
print(solution(77755))
