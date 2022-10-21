from typing import List


def solution(stack1: List[int], stack2: List[int], stack3: List[int]) -> str:
    moves = []

    stack4 = []
    disks = [0, stack1, stack2, stack3, stack4]

    while stack1 or stack2 or stack3:
        move = -1

        for i in range(1, 4):
            if disks[i] and (move == -1 or disks[i][-1] > disks[move][-1]):
                move = i

        moves.append(str(move))
        stack4.append(disks[move].pop())

    for i in range(1, 4):
        while disks[i]:
            moves.append(str(i))
            stack4.append(disks[i].pop())

    return ''.join(moves)


# print(solution([2, 7], [4, 5], [1]))
# print(solution([10, 20, 30], [8], [1]))
# print(solution([7], [], [9]))
# print(solution([7], [], [9]))
#print(solution([1, 2, 4], [3, 5, 6, 7, ], [8, 9]))
#print(solution([3, 4, 1000], [5], [1]))
