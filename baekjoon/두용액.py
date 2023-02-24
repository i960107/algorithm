from typing import List, Tuple


def solution(N: int, liquids: List[int]) -> List[int]:
    liquids.sort()
    left, right = 0, N - 1
    final = [-1000000001, -10000000001]
    while left < right:

        if liquids[left] + liquids[right] == 0:
            return [liquids[left], liquids[right]]
        else:
            cur_sum = liquids[left] + liquids[right]
            final_sum = sum(final)
            if abs(final_sum) > abs(cur_sum):
                final = [liquids[left], liquids[right]]
            if cur_sum > 0:
                right -= 1
            else:
                left += 1
    return final


N = int(input())
liquids = list(map(int, input().split()))
print(*solution(N, liquids))
