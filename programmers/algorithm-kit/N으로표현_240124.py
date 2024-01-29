from collections import deque

def solution(N, number):
    S = [{N}]
    for i in range(2, 9):
        lst = [int(str(N)*i)]
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
    queue = deque()
    queue.append((N, 1))

    visited = set()
    while queue:
        num, count = queue.popleft()
        if num == number:
            return count
        if count == 8:
            continue
        if num in visited:
            continue
        visited.add(num)
        queue.append((num + N, count + 1))
        queue.append((num - N, count + 1))
        queue.append((num // N, count + 1))
        queue.append((num * N, count + 1))
        queue.append((num * 10 + num, count + 1))
    return -1


print(solution(5, 12))  # 4
print(solution(2, 11))  # 4
