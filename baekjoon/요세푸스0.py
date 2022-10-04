from typing import List


def test(N: int, k: int) -> List[int]:
    answer = []

    arr = [i for i in range(1, N + 1)]
    pos = -1

    while len(answer) < N:
        curr_k = 0
        while curr_k != k:
            pos = (pos + 1) % len(arr)
            if arr[pos] != 0:
                curr_k += 1

        answer.append(arr[pos])
        arr[pos] = 0

    return answer


print(test(7, 3))
