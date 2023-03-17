import copy
from collections import deque
from typing import Deque

'''소수경로'''


class State:
    def __init__(self, value: int, depth: int):
        self.value = value
        self.depth = depth


# number에서 한 글자를 변경해 만둘 수 있는 모든 1000 ~ 9999 사이의 소수를 반환
def get_adjacent_prime_numbers(number: int) -> Deque[int]:
    adjacent_prime_numbers = deque()

    org_digits = [0] * 4
    org_digits[0] = number // 1000
    org_digits[1] = (number % 1000) // 100
    org_digits[2] = (number % 100) // 10
    org_digits[3] = number % 10

    for pos in range(4):
        new_digits = copy.deepcopy(org_digits)
        for digit in range(0, 10):
            new_digits[pos] = digit

            new_integer = new_digits[0] * 1000 + new_digits[1] * 100 + new_digits[2] * 10 + new_digits[3]
            if 1000 <= new_integer <= 9999 and is_prime[new_integer] and new_integer != number:
                adjacent_prime_numbers.append(new_integer)

    return adjacent_prime_numbers


def test_case(case_index: int):
    origin, dest = map(int, input().split())

    visited = [False] * MAX_NUMBER
    distance = [0] * (MAX_NUMBER + 1)

    bfs_queue = deque()
    initial_state = State(origin, 1)
    bfs_queue.append(initial_state)

    while bfs_queue:
        current = bfs_queue.popleft()

        if visited[current.value]:
            continue

        visited[current.value] = True
        distance[current.value] = current.depth - 1

        if current.value == dest:
            break

        for next in get_adjacent_prime_numbers(current.value):
            if visited[next]:
                continue
            next_state = State(next, current.depth + 1)
            bfs_queue.append(next_state)

    if not visited[dest]:
        print("Impossible")
    else:
        answer = distance[dest]
        print(answer)


def fill_sieve():
    is_prime[0] = False
    is_prime[1] = False

    for p in range(2, MAX_NUMBER + 1):
        if not is_prime[p]:
            continue
        for mul in range(p * 2, MAX_NUMBER + 1, p):
            is_prime[mul] = False


MAX_NUMBER = 10000

is_prime = [True] * (MAX_NUMBER + 1)
fill_sieve()

case_size = int(input())

for case_index in range(1, case_size + 1):
    test_case(case_index)
