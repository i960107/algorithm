import itertools
from typing import List


def permute_fail(nums: List[int]) -> List[List[int]]:
    def dfs(index: int, path: List[int]):
        if len(path) == len(nums):
            answer.append(path)
            return

        for i in range(index, len(nums)):
            # path 공유되는 문제가 있음...
            path = path + [i]
            dfs(index + 1, path)

    answer = []
    if not nums:
        return answer

    dfs(0, [])

    return answer


def permute(nums: List[int]) -> List[List[int]]:
    result = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드일때 결과 추가
        if len(elements) == 0:
            result.append(prev_elements[:])
            # list slicing하는 것과 어떻게 다르지?
            # 결과 값이 추가되는 게 아니라rev_elements에 대한 참조가 추가되며, 참조된 값이 변경될 경우 같이 바뀌게 된다.
            # result.append(prev_elements)

        # 순열의 상태 전달 그래프에서 레벨이 증가할 수록 자식 노드의 개수를 점점 작아진다.(순열의 수식 형태와 같음)
        for e in elements:
            next_elements = elements[:]
            # O(N)
            next_elements.remove(e)
            prev_elements.append(e)
            dfs(next_elements)
            # 언제 재귀 호출을 종료하고 빠져나오지?
            # 재귀 호출 하나씩 종료되면서 prev_elements원소 뒤에서부터 삭제됨.
            # prev_elements를 다음 for문에서도 써야되므로!
            prev_elements.pop()

    dfs(nums)
    return result

def test(nums: List[int]) -> List[List[int]]:
    answer= []
    def dfs(path:List[int]):
        if len(path) == len(nums):
            answer.append(path[:])
            return
        for i in range(len(nums)):
    dfs([])
    return answer

def itertools_permute(nums: List[int]) -> List[List[int]]:
    # 코딩 테스트시에 활용한다면, 구현의 효율성, 성능을 위해 사용했따는 설명을 달아두기!
    # permutations는 tuple의 sequence를 generate함
    return list(map(list, itertools.permutations(nums)))


print(permute([1, 2, 3]))
