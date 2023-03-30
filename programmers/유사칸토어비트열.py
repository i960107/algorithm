def solution(n: int, l: int, r: int) -> int:
    d = {
        0: 1,
        1: 1,
        2: 0,
        3: 1,
        4: 1,
    }

    count = 0
    first_0_index = (2 * 5 ** (n - 2)) * 5
    last_0_index = first_0_index + (5 ** (n - 2)) * 5 - 1
    for order in range(l, r + 1):
        index = order - 1
        if n != 1 and first_0_index <= index <= last_0_index:
            continue
        if d[index % 5] == 1:
            count += 1
    return count


print(solution(2, 4, 17))
