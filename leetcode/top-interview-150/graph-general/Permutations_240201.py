from typing import List
from copy import deepcopy
from itertools import permutations


def permute(nums: List[int]) -> List[List[int]]:
    answer = []
    path = []
    visited = set()

    length = len(nums)

    def dfs():
        # variable shadow: occurs when local scope variable has same name as outer scope variable
        # 같은 이름의 변수 선언되면 덮어써짐.
        if len(path) == length:
            answer.append(deepcopy(path))
            return

        for n in nums:
            if n in visited:
                continue
            path.append(n)
            visited.add(n)
            dfs()
            path.pop()
            visited.remove(n)

    dfs()

    return answer


def permute2(nums: List[int]) -> List[List[int]]:
    return [list(x) for x in permutations(nums)]


print(permute2([1, 2, 3]))
