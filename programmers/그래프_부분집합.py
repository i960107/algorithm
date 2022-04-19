from typing import List


def solution_mine(nums: List[int]) -> List[List[int]]:
    results = []

    def subset(k: int, index: int, path: List[int]):
        if len(path) == k:
            results.append(path)
            return
        for i in range(index, len(nums)):
            # 중복조합이 안되도록 조심!
            # subset(k, index + 1, path + [nums[i]])
            subset(k, i + 1, path + [nums[i]])

    for k in range(len(nums) + 1):
        subset(k, 0, [])

    return results


print("테스트", solution_mine([1, 2, 3]))


def solution(nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(index, path):
        # 매번 결과 추가
        result.append(path)

        # k개를 매개변수로 넘겨주는게 아니라! 경로를 만들면서 DFS
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


print(solution([1, 2, 3]))
