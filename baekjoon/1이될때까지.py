def solution(N: int, K: int) -> int:
    count = 0

    while N != 1:

        target = N // K * K

        if target != 0:
            count += (N - target)
            N = target

        N //= K
        count += 1

    return count


res = solution(25, 5)
print(res == 2)
