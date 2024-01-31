from collections import deque


def solution(N, number):
    S = [{N}]
    for i in range(2, 9):
        lst = [int(str(N) * i)]
        for X_i in range(0, int(i / 2)):
            for x in S[X_i]:
                for y in S[i - X_i - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1


def solution2(N: int, number: int) -> int:
    # 4 ^ 7승 -> brute force도 충분히 가능
    # 최단거리 -> bfs
    # 단순히 bfs만으로는 괄호 처리 불가능.

    n = 8
    dp = [set() for _ in range(n + 1)]
    num = 0

    answer = -1
    for i in range(1, n + 1):
        num = num * 10 + N
        dp[i].add(num)

    # for i in range(1, n):
    #     for j in range(1, i):
    #         for num1 in dp[j]:
    #             for num2 in dp[i - 1 - j]:
    #                 dp[i].add(num1 + num2)
    #                 dp[i].add(num1 - num2)
    #                 dp[i].add(num1 * num2)
    #                 if num2 != 0:
    #                     dp[i].add(num1 // num2)
    for i in range(1, n + 1):
        for j in range(1, i // 2 + 1):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num2 - num1)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                    if num1 != 0:
                        dp[i].add(num2 // num1)
        if number in dp[i]:
            answer = i
            break

    return answer


print(solution2(5, 12))  # 4
print(solution2(2, 11))  # 3
print(solution2(2, 32000))  # 3
print(solution2(1, 32000))  # 3
